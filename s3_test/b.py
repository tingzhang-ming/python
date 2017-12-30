import os
import hashlib
import boto3
import botocore.exceptions


CHUNK_SIZE = 2 ** 4


class StreamReader(object):
    """Wrap the stream from the backup process and chunk it into segements."""

    def __init__(self, stream, filename, **kwargs):
        self.stream = stream
        self.filename = filename
        self.container = self.filename
        self.segment_length = 0
        self.process = None
        self.file_number = 0
        self.end_of_file = False
        self.segment_checksum = hashlib.md5()
        self.size = kwargs.setdefault('size', 0)
        self.update_fun = kwargs.setdefault('update_fun', None)
        self.chunk_sum = 0
        self.position = 0
        self.latest_chunk = ''

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
        if self.position < self.segment_length:
            self.position = self.segment_length
            return self.latest_chunk
        chunk = self.stream.read(chunk_size)
        if not chunk:
            self.end_of_file = True
            return ''
        self.segment_checksum.update(chunk)
        self.segment_length += len(chunk)
        self.position = self.segment_length
        self.latest_chunk = chunk
        return chunk

    def tell(self):
        return self.position

    def seek(self, position):
        self.position = position


class MockStream(object):

    def __init__(self, max_n):
        self.max = max_n
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return str(r)
        raise StopIteration()


# os.environ['http_proxy'] = '109.105.4.17:8119'
os.environ['https_proxy'] = '109.105.4.17:8119'

s3 = boto3.resource('s3',
                    region_name='us-east-1',
                    aws_access_key_id='',
                    aws_secret_access_key='')

data = open('/root/github/python/s3_test/test.txt', 'rb')
stream = StreamReader(data, 'test.txt')
s3.Bucket('dbelt').put_object(Key='test.jpg', Body=stream)
data.close()
# for i in MockStream(10):
#     print i
