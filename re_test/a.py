import re

text = 'The quick brown fox jumped...'


def t1():
    match = re.search(r'fox', text)
    print match.group()
    # fox


def t2():
    print re.findall(r'o', text)
    for i in re.finditer(r'o', text):
        print i.group()
    # ['o', 'o']
    # o
    # o


def t3():
    match = re.search(r'fox', text)
    print match.group()
    # fox

if __name__ == '__main__':
    t3()
