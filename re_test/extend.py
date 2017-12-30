# encoding: utf-8
import re


# 忽略大小写 = re.I/IGNORECASE
def t1():
    print re.findall('(?i)yes', 'yes? Yes. YES!!')
    # ['yes', 'Yes', 'YES']


def t2():
    print re.findall('(?i)th\w+', 'The quickest way is through this tunnel.')
    # ['The', 'through', 'this']

data = """
This line is the first, 
another line, 
that line, it's the best
"""


# 多行混合 = re.M/MULTILINE
def t3():
    print re.findall('(?im)(^th[\w ]+)', data)
    # ['This line is the first', 'that line']


# . 可以匹配\n = re.S/DOTALL
def t4():
    print re.findall('(?i)th.+', data)
    print re.findall('(?is)th.+', data)
    # ['This line is the first, ', 'ther line, ', "that line, it's the best"]
    # ["This line is the first, \nanother line, \nthat line, it's the best\n"]


# 忽略表达式中的空格 = re.X/VERBOSE
def t5():
    patt = '''(?x)
\((\d{3})\)  # 区号
[ ]          # 空白符
(\d{3})      # 前缀
-            # 横线
(\d{4})      # 终点数字
'''
    print re.search(patt, '(800) 555-1212').groups()


def t6():
    data = 'http://google.com http://www.google.com http://code.google.com'
    print re.findall('http://(?:\w+\.)*(\w+\.com)', data)
    print re.findall('http://(\w+\.)*(\w+\.com)', data)
    print '--------------------------'
    for i in re.finditer('http://(?:\w+\.)*(\w+\.com)', data):
        print i.group()
    print '--------------------------'
    for i in re.finditer('http://(\w+\.)*(\w+\.com)', data):
        print i.group()
    # ['google.com', 'google.com', 'google.com']
    # [('', 'google.com'), ('www.', 'google.com'), ('code.', 'google.com')]
    # --------------------------
    # http: // google.com
    # http: // www.google.com
    # http: // code.google.com
    # --------------------------
    # http: // google.com
    # http: // www.google.com
    # http: // code.google.com


def t7():
    patt = '\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})'
    print re.search(patt, '(800) 555-1212').groupdict()
    # {'areacode': '800', 'prefix': '555'}


def t8():
    patt = '\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})'
    print re.sub(patt, '(\g<areacode>) \g<prefix>-xxx', '(800) 555-1212')
    # (800) 555-xxx


def t9():
    data = '''
    Guido van Rossum
    Tim Peters
    Alex Martelli
    Just van Rossum
    Raymond Hettinger
    '''
    print re.findall('\w+(?= van Rossum)', data)
    # ['Guido', 'Just']


def t10():
    data = '''
     sales@phptr.com
     postmaster@phptr.com
     eng@phptr.com
     noueply@phptr.com
     admin@phptr.com
    '''
    print re.findall('(?m)^\s+(?!noueply|postmaster)(\w+)', data)
    # ['sales', 'eng', 'admin']


def t11():
    data = '''
     sales@phptr.com
     postmaster@phptr.com
     eng@phptr.com
     noueply@phptr.com
     admin@phptr.com
    '''
    print ['%s@aw.com' % e.group(1) for e in re.finditer('(?m)^\s+(?!noueply|postmaster)(\w+)', data)]
    # ['sales@aw.com', 'eng@aw.com', 'admin@aw.com']


# 匹配两个紧挨着不重复
def t12():
    print bool(re.search('(?:(x)|y)(?(1)y|x)', 'xy'))
    print bool(re.search('(?:(x)|y)(?(1)y|x)', 'xx'))
    # True
    # False


if __name__ == '__main__':
    t12()
