# -*- coding:utf-8 -*-
import time


def t1():
    # 当前时间
    print time.time()
    # 时间戳形式
    print time.localtime(time.time())
    # 简单可读形式
    print time.asctime(time.localtime(time.time()))
    # 格式化成2016-03-20 11:45:39形式
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 格式化成Sat Mar 28 22:24:24 2016形式
    print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
    # 将格式字符串转换为时间戳
    a = "Sat Mar 28 22:24:24 2016"
    print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))


def t2():
    print "{} 00:00:00".format(time.strftime("%Y-%m-%d", time.localtime()))

if __name__ == '__main__':
    t2()
