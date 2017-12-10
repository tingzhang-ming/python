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
