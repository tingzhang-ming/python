import re


def t1():
    data = 'dfsdfdf industry fdfsdf industries sdfgfgsd  industriesdd'
    patt = 'industr(?:y|ies)'
    print re.findall(patt, data)
    # ['industry', 'industries', 'industries']


def t2():
    data = 'dfsdfdf industry fdfsdf industries sdfgfgsd industriesdd'
    patt = 'industry|industries'
    print re.findall(patt, data)
    # ['industry', 'industries', 'industries']


def t3():
    data = 'dfsdfdf industry fdfsdf industries sdfgfgsd industriesdd'
    patt = 'industr(?=(?:y|ies))'
    print re.findall(patt, data)


def t4():
    data = 'haha2 dgfdfgdgsdf34546456757 6785685 haha0lala'
    patt = '(?<=haha).{1,200}(?=lala)'
    print re.findall(patt, data)


if __name__ == '__main__':
    t4()


