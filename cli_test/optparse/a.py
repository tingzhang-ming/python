import optparse


def t1():
    parser = optparse.OptionParser()
    options, args = parser.parse_args()
    print args
    print options
    # [root @ mhc optparse]  # python a.py hahah lala
    # ['hahah', 'lala']
    # {}


def t2():
    parser = optparse.OptionParser()
    parser.add_option('-q',
                      '--quiet',
                      action='store_true',
                      dest='quiet',
                      help='Suppress output.')
    parser.add_option('-H',
                      '--host',
                      default='localhost',
                      dest='host',
                      help='The host to connect to. Defaults to localhost',
                      type=str)
    parser.add_option('-p',
                      '--port',
                      default=5432,
                      dest='port',
                      help='The port to connect to. Defaults to 5432',
                      type=int)
    options, args = parser.parse_args()
    print args
    print options
"""
[root@mhc optparse]# python a.py -h
Usage: a.py [options]

Options:
  -h, --help   show this help message and exit
  -q, --quiet  Suppress output.

[root@mhc optparse]# python a.py hahah lala --quiet -H mm
['hahah', 'lala']
{'host': 'mm', 'quiet': True}

"""


def t3():
    parser = optparse.OptionParser()
    parser.add_option('-v',
                      action='count',
                      default=0,
                      dest='verbosity',
                      help='Be more verbose. This flat may be repeated.')
    options, args = parser.parse_args()
    print 'The verbosity level is %d.' % options.verbosity


"""
[root@mhc optparse]# python a.py -vvv
The verbosity level is 3.
[root@mhc optparse]# python a.py -v -v -v
The verbosity level is 3.
[root@mhc optparse]# python a.py -v -v
The verbosity level is 2.
"""


def t4():
    parser = optparse.OptionParser()
    parser.add_option('-u',
                      '--user',
                      action='append',
                      default=[],
                      dest='users',
                      help='The username to be printed. Provide this multiple times to '
                           'print the username for multiple users.')
    options, args = parser.parse_args()
    for user in options.users:
        print 'Username: %s' % user
"""
[root@mhc optparse]# python a.py -umhc --user haha --user=lala -u=mememe
Username: mhc
Username: haha
Username: lala
Username: =mememe
"""


def t5():
    parser = optparse.OptionParser()
    parser.add_option('-q',
                      '--quiet',
                      action='store_true',
                      dest='quiet',
                      help='Suppress output.')
    parser.add_option('-H',
                      '--host',
                      action='store_false',
                      dest='host',
                      default=True,
                      help='The host to connect to. Defaults to localhost')
    options, args = parser.parse_args()
    print options.quiet
    print options.host

"""
[root@mhc optparse]# python a.py -q -H
True
False
[root@mhc optparse]# python a.py -q
True
True
"""


if __name__ == '__main__':
    t5()
