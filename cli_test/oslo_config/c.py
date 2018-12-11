from oslo_config import cfg

CONF = cfg.CONF


class BaseApp(object):

    name = None

    @classmethod
    def add_argument_parser(cls, subpasers):
        parser = subpasers.add_parser(cls.name, help=cls.__doc__)
        parser.set_defaults(cmd_class=cls)
        return parser


class Test1(BaseApp):
    """This is test1 command"""

    name = "test1"

    @classmethod
    def add_argument_parser(cls, subparsers):
        parser = super(Test1, cls).add_argument_parser(subparsers)
        parser.add_argument(
            '--t_a',
            default='haha',
            help='lalal'
        )

    @staticmethod
    def main():
        print("test1 command")
        print(CONF.command.t_a)


class Test2(BaseApp):
    """This is test2 command"""

    name = "test2"

    @classmethod
    def add_argument_parser(cls, subparsers):
        parser = super(Test2, cls).add_argument_parser(subparsers)
        parser.add_argument(
            '--t_b',
            default='haha2',
            help='lalal2'
        )

    @staticmethod
    def main():
        print("test2 command")
        print(CONF.command.t_b)


CMDS = [
    Test1,
    Test2
]


def add_command_parsers(subparsers):
    for cmd in CMDS:
        cmd.add_argument_parser(subparsers)


command_opt = cfg.SubCommandOpt('command',
                                title='Commands',
                                help='Available commands',
                                handler=add_command_parsers)


def main(argv=None):
    CONF.register_cli_opt(command_opt)
    CONF(args=argv[1:],
         project='mhc',
         version="1.0",
         usage='%(prog)s [' + '|'.join([cmd.name for cmd in CMDS]) + ']',
         default_config_files=None)
    CONF.command.cmd_class.main()


if __name__ == '__main__':
    import sys
    main(sys.argv)

"""
python c.py -h
usage: c [test1|test2]

optional arguments:
  -h, --help          show this help message and exit
  --config-dir DIR    Path to a config directory to pull `*.conf` files from.
                      This file set is sorted, so as to provide a predictable
                      parse order if individual options are over-ridden. The
                      set is parsed after the file(s) specified via previous
                      --config-file, arguments hence over-ridden options in
                      the directory take precedence.
  --config-file PATH  Path to a config file to use. Multiple config files can
                      be specified, with values in later files taking
                      precedence. Defaults to None.
  --version           show program's version number and exit

Commands:
  {test1,test2}       Available commands
    test1             This is test1 command
    test2             This is test2 command
----------------------
python c.py test1 --t_a=2b
test1 command
2b
---------------------
python c.py test2 --t_b=34
test2 command
34

"""