# encoding: utf-8
import re

text = """<br/>您好，非常好，很开心认识你
<br/><a target=_blank href="www.baidu.com">百度一下</a>百度才知道
<br/><a target=_blank href="/view/fafa.htm">发发</ a>最佳帅哥
<br/><a target=_blank href="/view/lili.htm">丽丽</ a>最佳美女
<br/>
"""


def t1():
    # 匹配，捕获(存储)
    patt = '(?<=(href=")).{1,200}(?=(">))'
    print re.findall(patt, text)
    # [('href="', '">'), ('href="', '">'), ('href="', '">')]


def t2():
    # 匹配，不捕获(不存储)
    patt = '(?<=(?:href=")).{1,200}(?=(?:">))'
    print re.findall(patt, text)
    # ['www.baidu.com', '/view/fafa.htm', '/view/lili.htm']


def t3():
    # 匹配，捕获(存储)
    patt = '(?<=href=").{1,200}(?=">)'
    print re.findall(patt, text)
    # ['www.baidu.com', '/view/fafa.htm', '/view/lili.htm']

if __name__ == '__main__':
    t3()
