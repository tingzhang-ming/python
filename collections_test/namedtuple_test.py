from collections import namedtuple


def t1():
    User = namedtuple('User', ['name', 'sex', 'age'])

    user = User(name='mhc', sex='man', age=18)
    print user
    print user.name
    print user.age
    user = user._replace(age=22)
    print user
    # User(name='mhc', sex='man', age=18)
    # mhc
    # 18
    # User(name='mhc', sex='man', age=22)


def t2():
    User = namedtuple('User', ['name', 'sex', 'age'])

    user = User._make(['mhc', 'man', 11])
    print user
    print user.name
    print user.age
    # User(name='mhc', sex='man', age=11)
    # mhc
    # 11


def t3():
    User = namedtuple('User', ['name', 'sex', 'age'])
    a = dict(name='mhc', sex='man', age=18)
    user = User(**a)
    print user
    print user.name
    print user.age
    # User(name='mhc', sex='man', age=18)
    # mhc
    # 18


def t4():
    User = namedtuple('User', ['name', 'sex', 'age'])

    user = User(name='mhc', sex='man', age=18)
    print user
    print user.name
    print user.age
    user_d = user._asdict()
    print user_d
    print type(user_d)
    # User(name='mhc', sex='man', age=18)
    # mhc
    # 18
    # OrderedDict([('name', 'mhc'), ('sex', 'man'), ('age', 18)])
    # < class 'collections.OrderedDict'>


if __name__ == '__main__':
    t4()
