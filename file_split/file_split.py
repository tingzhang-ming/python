#!/usr/bin/python
import os
import sys
import errno
import hashlib
import shutil


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


def main(file_path, target_dir=None):
    if not target_dir:
        target_dir = os.path.dirname(file_path)
    if not os.path.isfile(file_path):
        print "file %s is not a file or not exist" % file_path
        sys.exit(1)
    safe_mkdir(target_dir)
    filename = os.path.basename(file_path)
    with open(file_path, 'rb') as stream:
        stream_reader = StreamReader(stream, filename, MAX_FILE_SIZE)
        while not stream_reader.end_of_file:
            stream_iterator = ReadableToIterable(stream_reader)
            file_path = os.path.join(target_dir, stream_reader.segment)
            with open(file_path, 'w') as f:
                f.write(next(stream_iterator))
            for data in stream_iterator:
                with open(file_path, 'a') as f:
                    f.write(data)


if __name__ == '__main__':
    target_file = target_dir = None
    if len(sys.argv) < 2:
        print "usage: %s [target_file] [target_dir]" % sys.argv[0]
        sys.exit(1)
    if len(sys.argv) > 1:
        target_file = sys.argv[1]
    if len(sys.argv) > 2:
        target_dir = sys.argv[2]
    main(target_file, target_dir)

"""
[root@mhc file_split]# export CHUNK_SIZE=1
[root@mhc file_split]# export MAX_FILE_SIZE=3
[root@mhc file_split]# python file_split.py /root/github/python/file_split/test.txt
[root@mhc file_split]# python file_split.py /root/github/python/file_split/test.txt /tmp/testdata

"""