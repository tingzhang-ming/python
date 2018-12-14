# coding: utf-8
import os
import pdfkit


def t1():
    pdfkit.from_url('http://daily.zhihu.com/story/9703448', '310.pdf')


def t2():
    pdfkit.from_url('http://daily.zhihu.com/story/9703448', 'D:\zhihu\\310.pdf')


def t3():
    try:
        pdfkit.from_url('http://daily.zhihu.com/story/9703448', 'D:/zhihu/310.pdf')
    except:
        pass
    src = 'D:/zhihu/310.pdf'
    if os.path.isfile(src):
        print "is file"
        os.rename('D:/zhihu/310.pdf', 'D:/zhihu/你好.pdf'.decode('utf-8'))


if __name__ == '__main__':
    t3()
