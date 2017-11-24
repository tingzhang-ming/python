import socket
from util import get_cmd


class Node(object):
    """
    Node represents the state of our running container and carries
    around the MySQL config, and clients for Consul and Snapshots.
    """
    def __init__(self, cp=None):
        self.cp = cp
        self.hostname = socket.gethostname()
        self.ip = "192.168.1.1"
        self.name = "node-{}".format(self.hostname)


def default(node, app_module=None):
    print "default in main......."


def cmd1(node, app_module=None):
    print "cmd1 in main.......%s" % node.name


def cmd2(node, app_module=None):
    cmd = get_cmd(app_module, "cmd_app")
    if cmd is not None:
        cmd(node)
        print "success"
    else:
        print "pass"
