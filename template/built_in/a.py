import string


def t1():
    a = string.Template('$who is $role')
    print a.substitute(who='daxin', role='Linux')
    print a.substitute(who='daxin', role='cat')


if __name__ == '__main__':
    t1()
