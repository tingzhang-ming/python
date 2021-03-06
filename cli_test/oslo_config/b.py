import sys
import inspect
from oslo_config import cfg

CONF = cfg.CONF


def custom_parser(parsername, parser):
    CONF.register_cli_opt(cfg.SubCommandOpt(parsername, handler=parser))


def parse_args(argv, default_config_files=None):
    cfg.CONF(args=argv[1:],
             project='trove',
             default_config_files=default_config_files)

# --------------------------------------------------------------------------


class Commands(object):

    def test1(self, t_a):
        print("test1 -----")
        print("t_a: %s" % t_a)

    def test2(self, t_b, t_c):
        print("test2 -----")
        print("t_b: %s, t_c: %s" % (t_b, t_c))

    def test3(self, t_d):
        print("test3 -----")
        print("t_a: %s" % t_d)
        # python2 b.py test3 sf
        # test3 - ----
        # t_a: sf

    def config(self, config_id, value_file, config_name=None, description=None):
        print(config_id)
        print(value_file)
        print(config_name)
        print(description)

    def execute(self):
        exec_method = getattr(self, CONF.action.name)
        args = inspect.getargspec(exec_method)
        args.args.remove('self')

        kwargs = {}
        for arg in args.args:
            kwargs[arg] = getattr(CONF.action, arg)
        exec_method(**kwargs)


def main():
    def actions(subparser):
        parser = subparser.add_parser('test1',
                                      help='Populate the database structure')
        parser.set_defaults(haha="lala")
        parser.add_argument('--t_a',
                            help='SQLAlchemy Migrate repository path')

        parser = subparser.add_parser('test2',
                                      help='Upgrade the database to the specified version')
        parser.add_argument('--t_b',
                            help='Target version. Defaults to the latest version')
        parser.add_argument('--t_c',
                            help='SQLAlchemy Migrate repository path')

        parser = subparser.add_parser('test3',
                                      help='Populate the database structure')
        parser.add_argument('t_d',
                            help='SQLAlchemy Migrate repository path')

        parser = subparser.add_parser("config")
        parser.add_argument('config_id')
        parser.add_argument('value_file', help='the config file path')
        parser.add_argument('--config_name', help='the config of name')
        parser.add_argument('--description', help='the config of desc')
    custom_parser('action', actions)
    parse_args(sys.argv)
    try:
        Commands().execute()
        sys.exit(0)
    except TypeError as e:
        print("Possible wrong number of arguments supplied %s" % e)
        sys.exit(2)
    except Exception:
        print("Command failed, please check log for more info.")
        raise


if __name__ == '__main__':
    main()
