from oslo_config import cfg, types

ListOfPortsType = types.Range(1, 65535)

common_opts = [
    cfg.IPOpt('bind_host', default='0.0.0.0',
              help='IP address the API server will listen on.'),
    cfg.PortOpt('bind_port', default=8779,
                help='Port the API server will listen on.'),
    cfg.StrOpt('api_paste_config', default="api-paste.ini",
               help='File name for the paste.deploy config for trove-api.'),
    cfg.BoolOpt('trove_volume_support', default=True,
                help='Whether to provision a Cinder volume for datadir.'),
    cfg.ListOpt('admin_roles', default=['admin'],
                help='Roles to add to an admin user.'),
]

database_opts = [
    cfg.StrOpt('connection',
               # default='sqlite:///trove_test.sqlite',
               default='mysql+pymysql://rds:Kingsoft@localhost/trove_test',
               help='SQL Connection.',
               secret=True),
    cfg.IntOpt('idle_timeout',
               default=3600),
]

mysql_group = cfg.OptGroup(
    'mysql', title='MySQL options',
    help="Oslo option group designed for MySQL datastore")
mysql_opts = [
    cfg.BoolOpt('icmp', default=False,
                help='Whether to permit ICMP.'),
    cfg.ListOpt('tcp_ports', default=["3306"], item_type=ListOfPortsType,
                help='List of TCP ports and/or port ranges to open '
                     'in the security group (only applicable '
                     'if trove_security_groups_support is True).')
]


CONF = cfg.CONF

CONF.register_opts(common_opts)

CONF.register_opts(database_opts, 'database')

CONF.register_group(mysql_group)

CONF.register_opts(mysql_opts, mysql_group)


def parse_args(argv, default_config_files=None):
    cfg.CONF(args=argv[1:],
             project='trove',
             version="1.0",
             default_config_files=default_config_files)


# --------------------------------------------------------------
def t1():
    import sys
    parse_args(sys.argv)

    print CONF.bind_host
    print CONF.bind_port
    print CONF.api_paste_config
    print CONF.trove_volume_support
    print CONF.admin_roles

    print CONF["bind_host"]

    print CONF.database.connection
    print CONF.database.idle_timeout

    print CONF.mysql.icmp
    print CONF.mysql.tcp_ports

# python a.py --config-file D:\github\python\cli_test\oslo_config\configs\a.conf
# python a.py --config-dir D:\github\python\cli_test\oslo_config\configs
# 1.2.3.4
# 2222
# bala
# True
# ['aa', 'bb', 'cc']
# 1.2.3.4
# mysql://localhost:3306/test
# 111
# False
# [xrange(3306, 11224)]


def t2():
    import sys
    parse_args(sys.argv)
    print CONF.bind_port
    print CONF["bind_port"]
    CONF.bind_port = 9999
    print CONF.bind_port
    print CONF["bind_port"]


if __name__ == '__main__':
    t2()
