import io
import logging as LOG
from six.moves import configparser


class MySQLConfParser(object):
    """MySQLConfParser"""

    def __init__(self, config):
        self.config = config

    def parse(self):
        good_cfg = self._remove_commented_lines(str(self.config))
        cfg_parser = configparser.ConfigParser()
        cfg_parser.readfp(io.BytesIO(str(good_cfg)))
        return cfg_parser.items("mysqld")

    def _remove_commented_lines(self, config_str):
        ret = []
        for line in config_str.splitlines():
            line_clean = line.strip()
            if line_clean.startswith('#'):
                continue
            elif line_clean.startswith('!'):
                continue
            elif line_clean.startswith(';'):
                continue
            # python 2.6 configparser doesnt like params without values
            elif line_clean.startswith('[') and line_clean.endswith(']'):
                ret.append(line_clean)
            elif line_clean and "=" not in line_clean:
                LOG.debug("fixing line without '=' in it: %s" % line_clean)
                ret.append(line_clean + " = 1")
            else:
                ret.append(line_clean)
        rendered = "\n".join(ret)
        return rendered


class PostgreSQLConfigParser(MySQLConfParser):

    def __init__(self, config):
        super(PostgreSQLConfigParser, self).__init__(config)

    def parse(self):
        good_cfg = self._remove_commented_lines(str(self.config))
        res = []
        for line in good_cfg.splitlines():
            line_split = line.split('=')
            res.append((line_split[0].strip(), line_split[1].strip()))
        return res


def t1():
    p = "./confs/mysql.template"
    with open(p) as f:
        config = f.read()
    mc = MySQLConfParser(config)
    r = mc.parse()
    rr = dict(r)
    print rr
    for k, v in rr.iteritems():
        print "k: %s, v: %s" % (k, v)


def t2():
    p = "./confs/pg.template"
    with open(p) as f:
        config = f.read()
    mc = PostgreSQLConfigParser(config)
    r = mc.parse()
    print r
    rr = dict(r)
    print rr
    for k, v in rr.iteritems():
        print "k: %s, v: %s" % (k, v)


if __name__ == '__main__':
    t2()
