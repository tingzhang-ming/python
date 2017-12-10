# encoding: utf-8
import subprocess


class ShellException(Exception):

    def __init__(self, code, stdout='', stderr=''):
        self.code = code
        self.stdout = stdout
        self.stderr = stderr

    def __str__(self):
        return 'exit code %d - %s' % (self.code, self.stderr)


def run_command(command):

    proc = subprocess.Popen(command.split(' '),
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    proc.wait()

    stdout, stderr = proc.communicate()
    if proc.returncode > 0:
        raise ShellException(proc.returncode, stdout.strip(), stderr.strip())

    return stdout.strip()


class AcceptableErrorCodes(object):

    def __init__(self, *error_codes):
        self.error_codes = error_codes

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_type:
            return True
        if not issubclass(exc_type, ShellException):
            return False
        return exc_val.code in self.error_codes


def t1():
    with AcceptableErrorCodes(1):
        run_command("rm sdfsdfsfg")
    print '----------------------'
    run_command("rm sdfsdfsfg")
# ----------------------
# Traceback (most recent call last):
#   File "/root/github/python/with_test/c.py", line 54, in <module>
#     t1()
#   File "/root/github/python/with_test/c.py", line 49, in t1
#     run_command("rm sdfsdfsfg")
#   File "/root/github/python/with_test/c.py", line 24, in run_command
#     raise ShellException(proc.returncode, stdout.strip(), stderr.strip())
# __main__.ShellException: exit code 1 - rm: 无法删除"sdfsdfsfg": 没有那个文件或目录


import contextlib


@contextlib.contextmanager
def acceptable_error_codes(*codes):
    try:
        yield
    except ShellException as exc_instance:
        if exc_instance.code not in codes:
            raise


def t2():
    with acceptable_error_codes(1):
        run_command("rm sdfsdfsfg")

if __name__ == '__main__':
    t2()
