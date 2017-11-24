from app import Node


class MyNode(Node):
    """
    Node represents the state of our running container and carries
    around the MySQL config, and clients for Consul and Snapshots.
    """
    def __init__(self, cp=None, client=None):
        super(MyNode, self).__init__(cp)
        self.client = client

    def p(self):
        print self.name
        print self.client


def _new_node():
    return MyNode(cp="cp", client="mysql")


def default(node):
    print "default in app......."


def cmd1(node):
    print "cmd1 in app.......%s" %node.name


def cmd_app(node):
    node.p()
