#!/usr/bin/python
import sys
import logging as log
from oslo_utils import importutils
from util import get_cmd


def main(base, *args):
    app_base = importutils.import_module(base)
    app = importutils.import_module(app_path)
    get_node = get_cmd(app, "_new_node")
    if get_node is not None:
        node = get_node()
    else:
        node_path = "{}.Node".format(app_base_path)
        node = importutils.import_object(node_path, cp="haha")

    if len(sys.argv) == 1:
        cmd_name = "default"
    else:
        cmd_name = sys.argv[1]
    base_cmd = get_cmd(app_base, cmd_name)
    cmd = get_cmd(app, cmd_name)
    if base_cmd is None and cmd is None:
        log.error('Invalid command: %s', sys.argv[1])
        sys.exit(1)
    if base_cmd is not None:
        base_cmd(node, app)
    if cmd is not None:
        cmd(node)

if __name__ == '__main__':
    APP_BASE = "app"
    main(APP_BASE, "app.a_app")
