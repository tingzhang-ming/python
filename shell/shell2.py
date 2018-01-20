import os
import subprocess


class ShellException(Exception):
    def __init__(self, code, stdout='', stderr=''):
        self.code = code
        self.stdout = stdout
        self.stderr = stderr

    def __str__(self):
        return 'exit code %d - %s' % (self.code, self.stderr)


def run_command(command):
    print command.split(' ')
    proc = subprocess.Popen(command,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True)
    proc.wait()
    print proc.pid

    stdout, stderr = proc.communicate()
    if proc.returncode > 0:
        raise ShellException(proc.returncode, stdout.strip(), stderr.strip())

    return stdout.strip()


def t1():
    os.killpg(11)
    run_command('')


if __name__ == '__main__':
    t1()
