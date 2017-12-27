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

if __name__ == '__main__':
    t6()
