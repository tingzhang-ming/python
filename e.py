import os


def t1():
    a = ''
    b = 'bb'
    print(a if a else b)


def get(name):
    name_split = name.split('/', 1)
    if len(name_split) > 1:
        return name_split[0], name_split[1]
    return name_split[0], ''


def t2():
    cases = ['deblt/dir/mhc',
             'deblt',
             'deblt/']
    for case in cases:
        print get(case)
    name = 'backs'
    for case in cases:
        bucket, path = get(case)
        print bucket
        print os.path.join(path, name)


if __name__ == '__main__':
    t2()
