import argparse


def t1():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-q',
        '--quiet',
        action='store_true',
        dest='quiet',
        help='Suppress output.'
    )
    args = parser.parse_args()
    print args.quiet
"""
[root@mhc argparse]# python a.py 
False
[root@mhc argparse]# python a.py -q
True
"""


def t2():
    parser = argparse.ArgumentParser(prefix_chars='/')
    parser.add_argument(
        '/q',
        '//quiet',
        action='store_true',
        dest='quiet',
        help='Suppress output.'
    )
    args = parser.parse_args()
    print args.quiet
"""
[root@mhc argparse]# python a.py -q
usage: a.py [/h] [/q]
a.py: error: unrecognized arguments: -q
[root@mhc argparse]# python a.py /q
True
"""


def t3():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-H',
        '--host',
        default='localhost',
        dest='host',
        help='The host to connect to. Defaults to localhost',
        type=str
    )
    args = parser.parse_args()
    print args.host
"""
[root@mhc argparse]# python a.py -Hmhc
mhc
[root@mhc argparse]# python a.py -H=mhc
mhc
[root@mhc argparse]# python a.py --host=mhc
mhc
[root@mhc argparse]# python a.py --host mhc
mhc
"""


def t4():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c',
        '--cheese',
        choices=('american', 'cheddar', 'provolone', 'swiss'),
        default='swiss',
        dest='cheese',
        help='The kind of cheese to use',
        type=str
    )
    args = parser.parse_args()
    print args.cheese

'''
[root@mhc argparse]# python a.py -h
usage: a.py [-h] [-c {american,cheddar,provolone,swiss}]

optional arguments:
  -h, --help            show this help message and exit
  -c {american,cheddar,provolone,swiss}, --cheese {american,cheddar,provolone,swiss}
                        The kind of cheese to use
[root@mhc argparse]# python a.py
swiss
[root@mhc argparse]# python a.py -c american
american
[root@mhc argparse]# python a.py -c americanss
usage: a.py [-h] [-c {american,cheddar,provolone,swiss}]
a.py: error: argument -c/--cheese: invalid choice: 'americanss' (choose from 'american', 'cheddar', 'provolone', 'swiss')
'''


def t5():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-v',
        action='count',
        default=0,
        dest='verbosity',
        help='Be more verbose. This flat may be repeated.'
    )
    args = parser.parse_args()
    print args.verbosity
"""
[root@mhc argparse]# python a.py -v
1
[root@mhc argparse]# python a.py -vvv
3
"""


def t6():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--madlib',
        default=['fox', 'dogs'],
        dest='madlib',
        help='Two words to place in the madlib.',
        nargs=2,
    )
    args = parser.parse_args()
    print 'The quick brown {0} jumped over the lazy {1}.'.format(*args.madlib)

"""
[root@mhc argparse]# python a.py
The quick brown fox jumped over the lazy dogs.
[root@mhc argparse]# 
[root@mhc argparse]# python a.py --madlib pirate ninjas
The quick brown pirate jumped over the lazy ninjas.
"""


def t7():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--addends',
        dest='addends',
        help='Integers to provide a sum of.',
        nargs='+',
        required=True,
        type=int,
    )
    args = parser.parse_args()
    print '%s = %d' % (
        ' + '.join([str(i) for i in args.addends]),
        sum(args.addends)
    )
"""
[root@mhc argparse]# python a.py
usage: a.py [-h] --addends ADDENDS [ADDENDS ...]
a.py: error: argument --addends is required
[root@mhc argparse]# python a.py --addends 1
1 = 1
[root@mhc argparse]# python a.py --addends 1 2
1 + 2 = 3
[root@mhc argparse]# python a.py --addends 1 2 3
1 + 2 + 3 = 6
"""


def t8():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'addends',
        help='Integers to provide a sum of.',
        nargs='+',
        type=int,
    )
    # parser.add_argument(
    #     'addends2',
    #     help='Integers to provide a sum of.',
    #     nargs='+',
    #     type=int,
    # )
    # parser.add_argument(
    #     'addends3',
    #     help='Integers to provide a sum of.',
    #     nargs='+',
    #     type=str,
    # )
    args = parser.parse_args()
    print '%s = %d' % (
        ' + '.join([str(i) for i in args.addends]),
        sum(args.addends)
    )
    print args.addends2
    print args.addends3
"""
[root@mhc argparse]# python a.py addends 1 2 3
usage: a.py [-h] addends [addends ...]
a.py: error: argument addends: invalid int value: 'addends'
[root@mhc argparse]# python a.py 1 2 3
1 + 2 + 3 = 6
---------------------------
[root@mhc argparse]# python a.py 1 2 3
1 + 2 = 3
[3]
[root@mhc argparse]# python a.py 1 2 3
1 = 1
[2]
['3']

"""


def t9():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c',
        '--config-file',
        dest='config',
        help='The configuration file to use.',
        type=argparse.FileType('r'),
    )
    args = parser.parse_args()
    print args.config.read()

"""
[root@mhc argparse]# echo "This is my config file." > foo.txt
[root@mhc argparse]# python a.py -c foo.txt
This is my config file.
"""


if __name__ == '__main__':
    t9()
