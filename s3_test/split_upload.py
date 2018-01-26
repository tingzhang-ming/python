#!/usr/bin/python
import os
import sys
import errno
import hashlib
import shutil
import time
from threading import Thread, Event
import json
from Queue import Queue
import boto3
import re


def env(key, default, environ=os.environ, fn=None):
    """
    Gets an environment variable, trims away comments and whitespace,
    and expands other environment variables.
    """
    val = environ.get(key, default)
    try:
        val = val.split('#')[0]
        val = val.strip()
        val = os.path.expandvars(val)
    except (AttributeError, IndexError):
        # just swallow AttributeErrors for non-strings
        pass
    if fn:  # transformation function
        val = fn(val)
    return val


CHUNK_SIZE = env('CHUNK_SIZE', 2 ** 16, fn=int)
MAX_FILE_SIZE = env('MAX_FILE_SIZE', 5 * 1024 * 1024, fn=int)


class ReadableToIterable(object):
    """
    Wrap a filelike object and act as an iterator.

    It is recommended to use this class only on files opened in binary mode.
    Due to the Unicode changes in Python 3, files are now opened using an
    encoding not suitable for use with the md5 class and because of this
    hit the exception on every call to next. This could cause problems,
    especially with large files and small chunk sizes.
    """

    def __init__(self, content, chunk_size=CHUNK_SIZE):
        """
        :param content: The filelike object that is yielded from.
        :param chunk_size: The max size of each yielded item.
        """
        self.content = content
        self.chunk_size = chunk_size

    def __next__(self):
        """
        Both ``__next__`` and ``next`` are provided to allow compatibility
        with python 2 and python 3 and their use of ``iterable.next()``
        and ``next(iterable)`` respectively.
        """
        if self.chunk_size:
            chunk = self.content.read(self.chunk_size)
        else:
            chunk = self.content.read()
        if not chunk:
            raise StopIteration

        return chunk

    def next(self):
        return self.__next__()

    def __iter__(self):
        return self


def safe_mkdir(directory, clean=False):
    """
        Ensure a directory is present.  If it's not there, create it.  If it is,
        no-op. If clean is True, ensure the directory is empty.
    """
    if clean:
        safe_rmtree(directory)
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def safe_rmtree(directory):
    """
        Delete a directory if it's present. If it's not present, no-op.
    """
    if os.path.exists(directory):
        shutil.rmtree(directory, True)


class StreamReader(object):
    """Wrap the stream from the backup process and chunk it into segements."""

    def __init__(self, stream, filename, max_file_size=MAX_FILE_SIZE, **kwargs):
        self.stream = stream
        self.filename = filename
        self.container = self.filename
        self.max_file_size = max_file_size
        self.segment_length = 0
        self.process = None
        self.file_number = 0
        self.end_of_file = False
        self.end_of_segment = False
        self.segment_checksum = hashlib.md5()
        self.size = kwargs.setdefault('size', 0)
        self.update_fun = kwargs.setdefault('update_fun', None)
        self.chunk_sum = 0

    @property
    def base_filename(self):
        """Filename with extensions removed."""
        return self.filename.split('.')[0]

    @property
    def segment(self):
        return '%s_%08d' % (self.base_filename, self.file_number)

    @property
    def first_segment(self):
        return '%s_%08d' % (self.base_filename, 0)

    @property
    def segment_path(self):
        return '%s/%s' % (self.container, self.segment)

    def read(self, chunk_size=CHUNK_SIZE):
        if self.end_of_segment:
            self.segment_length = 0
            self.segment_checksum = hashlib.md5()
            self.end_of_segment = False

        # Upload to a new file if we are starting or too large
        if self.segment_length > (self.max_file_size - chunk_size):
            self.file_number += 1
            self.end_of_segment = True
            return ''

        chunk = self.stream.read(chunk_size)
        if not chunk:
            self.file_number += 1
            self.end_of_file = True
            return ''

        self.segment_checksum.update(chunk)
        self.segment_length += len(chunk)
        return chunk


def main(local_file_path, bucket, remote_dir, target_dir=None):
    s3 = boto3.resource('s3',
                        endpoint_url=None,
                        region_name='us-east-1',
                        aws_access_key_id=env('AWS_KEY_ID', ''),
                        aws_secret_access_key=env('AWS_SECRET_KEY', ''))
    # s3 = boto3.resource('s3',
    #                     endpoint_url='http://109.105.4.65:9001',
    #                     region_name='us-east-1',
    #                     aws_access_key_id='IW89KKUNNXT1LGSS6GLB',
    #                     aws_secret_access_key='3xCkdgO3TDjeFVfr7kFHMCRoip0BDzmnVxIeeMyv')

    if not target_dir:
        target_dir = os.path.dirname(local_file_path)
    if not os.path.isfile(local_file_path):
        print "file %s is not a file or not exist" % local_file_path
        sys.exit(1)

    size = os.path.getsize(local_file_path)
    safe_mkdir(target_dir)
    filename = os.path.basename(local_file_path).split('.')[0]
    remote_dir = os.path.join(remote_dir, filename)

    old_files = []
    for obj in s3.Bucket(bucket).objects.all():
        patt = '(^%s)/.*[^/]' % remote_dir.rstrip('/')
        result = re.search(patt, obj.key)
        if result:
            old_files.append(result.group())
    if len(old_files) > 0:
        print "find old files:"
        for of in old_files:
            print of
        ny = raw_input("Do you want to delete this all? y/n")
        if ny != 'y':
            print "exit"
            sys.exit(0)
        for of in old_files:
            print "delete %s..." % of
            s3.Bucket(bucket).Object(of).delete()

    yu = 1 if size % MAX_FILE_SIZE > 0 else 0
    print "gen metedata..."
    file_number = size / MAX_FILE_SIZE + yu
    print "file_number: %s" % str(file_number)
    files = [os.path.join(remote_dir, '%s_%08d' % (filename, i)) for i in range(file_number)]
    metadata_path = os.path.join(remote_dir, 'metadata')
    s3.Bucket(bucket).put_object(Key=metadata_path, Body=json.dumps(files))
    print "metadata uploaded in remote path: %s" % metadata_path
    print "now import data can be started------------------------------"

    que = Queue(maxsize=file_number)
    stop_event = Event()

    def upload_thread():
        print "start upload thread..."
        while not stop_event.isSet() or not que.empty():
            qf = que.get()
            time.sleep(3)
            remote_path = os.path.join(remote_dir, os.path.basename(qf))
            print "upload file %s to remote %s" % (qf, remote_dir)
            with open(qf, 'rb') as qdata:
                s3.Bucket(bucket).put_object(Key=remote_path, Body=qdata)
            print "upload file success"
            os.remove(qf)
        print "all files uploaded, exit"

    Thread(target=upload_thread).start()

    with open(local_file_path, 'rb') as stream:
        stream_reader = StreamReader(stream, filename, MAX_FILE_SIZE)
        while not stream_reader.end_of_file:
            stream_iterator = ReadableToIterable(stream_reader)
            file_path = os.path.join(target_dir, stream_reader.segment)
            with open(file_path, 'w') as f:
                f.write(next(stream_iterator))
            for data in stream_iterator:
                with open(file_path, 'a') as f:
                    f.write(data)
            print "gen file %s success..." % os.path.basename(file_path)
            que.put(file_path)
    stop_event.set()
    print "Gen files done"


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print "usage: %s local_file_path bucket remote_dir" % sys.argv[0]
        print "export CHUNK_SIZE=10"
        print "export MAX_FILE_SIZE=100"
        print "export AWS_KEY_ID="
        print "export AWS_SECRET_KEY"
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3])
