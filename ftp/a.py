# encoding: utf-8
import os
import hashlib
from ftplib import FTP


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
        print chunk_size
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


# 登录
def t1():
    ftp = FTP()
    timeout = 30
    port = 21
    ftp.connect('109.105.4.65', port, timeout)  # 连接FTP服务器
    ftp.login('test', 'test')  # 登录
    print ftp.getwelcome()  # 获得欢迎信息
    ftp.quit()  # 退出FTP服务器


# upload
def t2():
    ftp = FTP()
    timeout = 30
    port = 21
    ftp.connect('109.105.4.65', port, timeout)  # 连接FTP服务器
    ftp.login('test', 'test')  # 登录
    print ftp.getwelcome()  # 获得欢迎信息
    ftp.cwd('mhc')  # 设置FTP路径
    path = '/root/github/python/s3_test/test.txt'
    ftp.storbinary('STOR ' + os.path.basename(path), open(path, 'rb'))  # 上传FTP文件
    ftp.quit()  # 退出FTP服务器


# upload
def t21():
    ftp = FTP()
    timeout = 30
    port = 21
    ftp.connect('109.105.4.65', port, timeout)  # 连接FTP服务器
    ftp.login('test', 'test')  # 登录
    print ftp.getwelcome()  # 获得欢迎信息
    ftp.cwd('mhc')  # 设置FTP路径
    path = '/root/github/python/s3_test/test.txt'
    stream = StreamReader(open(path, 'rb'), 'test.txt')
    ftp.storbinary('STOR ' + os.path.basename(path), stream)  # 上传FTP文件
    ftp.quit()  # 退出FTP服务器


# list
def t3():
    ftp = FTP()
    timeout = 30
    port = 21
    ftp.connect('109.105.4.65', port, timeout)  # 连接FTP服务器
    ftp.login('test', 'test')  # 登录
    print ftp.getwelcome()  # 获得欢迎信息
    ftp.cwd('mhc')  # 设置FTP路径
    print ftp.nlst()
    ftp.quit()  # 退出FTP服务器


# download
def t4():
    ftp = FTP()
    timeout = 30
    port = 21
    ftp.connect('109.105.4.65', port, timeout)  # 连接FTP服务器
    ftp.login('test', 'test')  # 登录
    print ftp.getwelcome()  # 获得欢迎信息
    ftp.cwd('mhc')  # 设置FTP路径
    path = '/root/github/python/ftp/test.txt'
    f = open(path, 'wb')  # 打开要保存文件
    filename = 'RETR test.txt'  # 保存FTP文件
    ftp.retrbinary(filename, f.write)  # 保存FTP上的文件
    f.close()
    ftp.quit()  # 退出FTP服务器


class TestWrite(object):

    def __init__(self):
        self.num = 0

    def write(self, data):
        print self.num
        print data
        self.num += 1


def t41():
    ftp = FTP()
    timeout = 30
    port = 21
    ftp.connect('109.105.4.65', port, timeout)  # 连接FTP服务器
    ftp.login('test', 'test')  # 登录
    print ftp.getwelcome()  # 获得欢迎信息
    ftp.cwd('mhc')  # 设置FTP路径
    f = TestWrite()
    filename = 'RETR test.txt'  # 保存FTP文件
    ftp.retrbinary(filename, f.write, blocksize=10)  # 保存FTP上的文件
    ftp.quit()  # 退出FTP服务器


# delete
def t5():
    ftp = FTP()
    timeout = 30
    port = 21
    ftp.connect('109.105.4.65', port, timeout)  # 连接FTP服务器
    ftp.login('test', 'test')  # 登录
    print ftp.getwelcome()  # 获得欢迎信息
    ftp.cwd('mhc')
    ftp.delete('test.txt')
    ftp.quit()  # 退出FTP服务器


def t51():
    ftp = FTP()
    timeout = 30
    port = 21
    ftp.connect('109.105.4.65', port, timeout)  # 连接FTP服务器
    ftp.login('test', 'test')  # 登录
    path = 'mhc'
    fs = ftp.nlst(path)
    for f in fs:
        print f
        ftp.delete(f)
    ftp.rmd(path)
    ftp.quit()  # 退出FTP服务器


# create multi directory
def t6():
    ftp = FTP()
    timeout = 30
    port = 21
    ftp.connect('109.105.4.65', port, timeout)  # 连接FTP服务器
    ftp.login('test', 'test')  # 登录
    path = 'mhc3/mm/ddf'
    paths = path.split('/')
    for path in paths:
        if path not in ftp.nlst():
            ftp.mkd(path)
        ftp.cwd(path)
    ftp.quit()  # 退出FTP服务器


if __name__ == '__main__':
    t51()

