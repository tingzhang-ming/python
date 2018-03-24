import os
import re
import boto3
import botocore.exceptions

# os.environ['http_proxy'] = '109.105.4.17:8119'
os.environ['https_proxy'] = '109.105.4.17:8118'

os.environ['LOG_LEVEL'] = 'DEBUG'

s3 = boto3.resource('s3',
                    # endpoint_url='http://109.105.4.65:9001',
                    region_name='us-east-1',
                    aws_access_key_id='',
                    aws_secret_access_key='')

# ValueError: Invalid endpoint: https://s3.region=us-east-1.amazonaws.com

for bucket in s3.buckets.all():
    print(bucket.name)


# upload
def t1():
    data = open('/root/github/python/s3_test/test.txt', 'rb')
    s3.Bucket('dbelt').put_object(Key='test.jpg', Body=data)
    data.close()
    # s3.upload_file(filename, bucket_name, filename)


def t11():
    data = open('/root/github/python/s3_test/test.txt', 'rb')
    s3.Bucket('dbelt').put_object(Key='mhc/test2.txt', Body=data)
    data.close()

# t11()


# delete
def t2():
    ob = s3.Bucket('dbelt').Object('test.jpg')
    ob.delete()


# t2()

def delete_all():
    path = "backups"
    client = s3.Bucket('dbelt')
    files = []
    for obj in client.objects.all():
        patt = '(^%s)/.*[^/]' % path.rstrip('/')
        result = re.search(patt, obj.key)
        if result:
            # files.append(result.group())
            print result.group()
            client.Object(result.group()).delete()
    # for f in files:
    #     print f
    print "========================="

# delete_all()


def list_files(path):
    client = s3.Bucket('dbelt')
    files = []
    for obj in client.objects.all():
        patt = '(^%s)/.*[^/]' % path.rstrip('/')
        result = re.search(patt, obj.key)
        if result:
            files.append(result.group())
    return files


for f in list_files("test/backups"):
    print f


def list_directory(path='test'):
    client = s3.Bucket('dbelt')
    directories = {}
    all_obs = client.objects.all()
    for obj in all_obs:
        patt = '(?<=(?:(^%s)/)).*(?=(?:/))' % path.rstrip('/')
        result = re.search(patt, obj.key)
        if result:
            dir_name = result.group()
            if dir_name not in directories:
                directories[dir_name] = 0
            if not obj.key.endswith('/') and hasattr(obj, 'size'):
                directories[dir_name] += obj.size
    return [{"name": k, "size": v} for k, v in directories.items()]


def list_all():
    client = s3.Bucket('dbelt')
    directories = {}
    all_obs = client.objects.all()
    for ob in all_obs:
        print ob.key

# for i in list_directory():
#     print i
# list_all()

def t21():
    ob = s3.Bucket('dbelt').Object('mhc/test.txt')
    ob.delete()


# download
def t3():
    try:
        s3.Bucket('dbelt').download_file('test/backups/testbackup/metadata', '/root/github/python/s3_test/d.txt')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

# t3()

class MockWrite(object):

    def write(self, text):
        print text


def t31():
    s3.Bucket('dbelt').download_fileobj('mhc/test.txt', MockWrite())


# list object
def t4():
    bucket = s3.Bucket('dbelt')
    print '-----------'
    for obj in bucket.objects.all():
        print(obj.key)
        print obj.size

# t4()

def get_files(d):
    res = []
    bucket = s3.Bucket('dbelt')
    for obj in bucket.objects.all():
        print obj.key
        if not obj.key.endswith('/') and os.path.dirname(obj.key) == d:
            res.append(obj.key)
    print res


def get_all_fils(d):
    res = []
    bucket = s3.Bucket('dbelt')
    for obj in bucket.objects.all():
        patt = '(^%s)/.*[^/]' % d.rstrip('/')
        result = re.search(patt, obj.key)
        if result:
            res.append(result.group())
            print result.group()

    # for r in res:
    #     print r


# t4()
# get_all_fils('test')


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

# for i in MockStream(10):
#     print i


def t12():
    data = open('/root/github/python/s3_test/test.txt', 'rb')
    s3.Bucket('dbelt').put_object(Key='mhc/test.txt', Body=MockStream(10))
    data.close()
