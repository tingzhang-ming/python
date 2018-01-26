#!/usr/bin/python
import os
import sys
import json
import botocore.exceptions
import boto3
import time


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


def download_file(bucket, remote, local):
    """ download file from remote to local if exist"""
    try:
        s3.Bucket(bucket).download_file(remote, local)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            return False
        else:
            raise
    else:
        return True


def main(target_dir, bucket, remote):
    print 'bucket: %s' % bucket
    print 'remote object: %s' % remote
    files = []
    metadata_path = os.path.join(remote, 'metadata')
    metadata_flag = True
    client = s3.Bucket(bucket)

    metadata_file = os.path.join(target_dir, 'metadata')
    try:
        if download_file(bucket, metadata_path, metadata_file):
            with open(metadata_file) as mf:
                files = json.loads(mf.read().strip())
            print "down metadata file successful: %s" % metadata_file
        else:
            metadata_flag = False
    except:
        metadata_flag = False

    if metadata_flag is False:
        for obj in client.objects.all():
            if not obj.key.endswith('/') and \
                            os.path.dirname(obj.key) == remote and \
                            obj.key != metadata_path:
                files.append(obj.key)
    files.sort()
    l = len(files)
    n = 1
    temp_dir = '/tmp'
    TMP_FILENAME = 'download_to_a_file_tmp'

    print "file number: %d" % l
    filename = os.path.basename(remote)
    local_file_path = os.path.join(target_dir, filename)
    if os.path.exists(local_file_path):
        print '%s exist, now cover it' % local_file_path

    temp_file = os.path.join(temp_dir, TMP_FILENAME)
    with open(local_file_path, 'w') as lf:
        for file_name in files:
            while not download_file(bucket, file_name, temp_file):
                time.sleep(2)

            with open(temp_file, 'rb') as f:
                stream_iterator = ReadableToIterable(f, chunk_size=CHUNK_SIZE)
                for data in stream_iterator:
                    lf.write(data)
            print "download %s done" % file_name
            print "process: %d" % (n * 100 / l)
            n += 1
    print "all done"
    print "output file: %s" % local_file_path


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print "usage: %s target_dir bucket remote" % sys.argv[0]
        print "export CHUNK_SIZE=10"
        print "export MAX_FILE_SIZE=100"
        print "export AWS_KEY_ID="
        print "export AWS_SECRET_KEY"
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3])
