import re


def t1():
    print re.sub('X', 'Mr. Smith', 'attn: X\n\nDear X, \n')
# attn: Mr. Smith
#
# Dear Mr. Smith,


def t2():
    print re.subn('X', 'Mr. Smith', 'attn: X\n\nDear X, \n')
    # ('attn: Mr. Smith\n\nDear Mr. Smith, \n', 2)

if __name__ == '__main__':
    t2()
