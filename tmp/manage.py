#!/usr/bin/python
""" dbelt dbcm manage main module """
import sys
import argparse
import subprocess
from inspect import isfunction
from dbelt.common.utils import log, env
from dbelt.common.importutils import import_module, import_object

NAME = 'dbcm-manage'
DEFAULT_CMD = 'pre_start'
HANDLER_NAMES = ['pre_start', 'on_start', 'post_start',
                 'on_stop', 'post_stop', 'on_change',
                 'health', 'once_healthy', 'exit_failed']


def get_less_cmd():
    try:
        cmd = subprocess.check_output('which less').strip()
    except (subprocess.CalledProcessError, OSError):
        return None
    return cmd


def lists(module_path, default_cmd=DEFAULT_CMD, all_flag=False, detail=False):
    """ list commands """
    commands = get_commands(module_path)
    show = ''
    for k, v in commands.items():
        if k.startswith('_') or not isfunction(v) or k == 'main':
            continue
        if not all_flag and k not in HANDLER_NAMES:
            continue
        if k == default_cmd:
            show += '- {} (default)\n'.format(k)
            if detail:
                show += "   {}\n".format(v.__doc__)
        else:
            show += '- {}\n'.format(k)
            if detail:
                show += "   {}\n".format(v.__doc__)
    if detail:
        less_cmd = get_less_cmd()
        if less_cmd:
            process = subprocess.Popen(less_cmd, shell=True,
                                       stdin=subprocess.PIPE,
                                       stdout=sys.stdout)
            process.communicate(input=show)
            sys.exit(0)
    print show.strip()
    sys.exit(0)


def run(module_path, default_cmd=DEFAULT_CMD):
    """ run command """
    commands = get_commands(module_path)
    get_node = commands.get('_new_node', None)
    if get_node is not None:
        node = get_node()
    else:
        print "_new_node function not found."
        sys.exit(1)
    if len(sys.argv) == 1:
        cmd_name = default_cmd
    else:
        cmd_name = sys.argv[1]
    try:
        cmd = commands[cmd_name]
    except KeyError:
        log.error('Invalid command: %s', cmd_name)
        sys.exit(1)
    cmd(node)


def get_commands(module_name):
    module_name_split = module_name.split('.')
    l = len(module_name_split)
    res = {}
    for i in range(l):
        a_module = '.'.join(module_name_split[:i+1])
        print a_module
        try:
            a_app = import_module('dbelt.managers.{}.manage'.format(a_module))
        except KeyError:
            print 'error'
            continue
        res.update({k: v for k, v in vars(a_app).items() if not k.startswith('__') and isfunction(v)})
    return res


def main():
    """ main function """
    parser = argparse.ArgumentParser(usage="{} [command]".format(NAME))
    parser.add_argument('-l', '--list',
                        help='list containerpilot handler commands',
                        action='store_true')
    parser.add_argument('-a', '--all',
                        help='list all commands',
                        action='store_true')
    parser.add_argument('-d', '--detail',
                        help='show commands doc string',
                        action='store_true')
    ns, _ = parser.parse_known_args()
    module_name = env('DBCM_ROLE', 'testApp')
    if ns.list:
        lists(module_name, detail=ns.detail)
    elif ns.all:
        lists(module_name, all_flag=True, detail=ns.detail)
    elif ns.detail:
        print "usage {} -l/a -d".format(NAME)
        sys.exit(0)
    try:
        run(module_name)
    except ImportError as e:
        log.error(e.message)

if __name__ == '__main__':
    main()
