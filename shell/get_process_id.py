import os
import signal
import subprocess


def get_process_id(*args):
    """ get process id by some keywords """
    try:
        cmd = "ps -ef|grep -v grep %s |awk '{print $2}'" \
              % " ".join(["|grep '{}'".format(a) for a in args])
        results_str = subprocess.check_output(cmd, shell=True).strip().split('\n')
        results = [int(i) for i in results_str]
    except (subprocess.CalledProcessError, TypeError, ValueError):
        return []
    else:
        return results


def kill_processes(*args):
    """ kill process by process id """
    try:
        for pid in args:
            os.killpg(pid, signal.SIGTERM)
    except OSError:
        pass
    except TypeError:
        raise TypeError('integer is required')


def t1():
    print get_process_id('consul watch', 'dump_task')


def t2():
    kill_processes(*[999, 998, 997])

if __name__ == '__main__':
    t2()
