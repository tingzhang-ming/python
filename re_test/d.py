import re


def t1():
    print re.split(':', 'str1:str2:str3')
    # ['str1', 'str2', 'str3']

data = (
    'Mountain View, CA 94040',
    'Sunnyvale, CA',
    'Los Altos, 94023',
    'Cupertino 95014',
    'Palo Alto CA'
)


def t2():
    for datum in data:
        print re.split(', | (?=(?:\d{5}|[A-Z]{2}))', datum)


def t21():
    return re.split(', | (?=(?:\d{5}|[A-Z]{2}))', data[0])


def t3():
    for datum in data:
        m = re.findall(' (?:\d{5}|[A-Z]{2})', datum)
        print m


def t4():
    for datum in data:
        m = re.split('(?:\d{5}|[A-Z]{2})', datum)
        print m


def t5():
    for datum in data:
        m = re.findall('.*(?=CA)', datum)
        print m


if __name__ == '__main__':
    t2()


