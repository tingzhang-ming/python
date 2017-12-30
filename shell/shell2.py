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

    stdout, stderr = proc.communicate()
    if proc.returncode > 0:
        raise ShellException(proc.returncode, stdout.strip(), stderr.strip())

    return stdout.strip()


def t1():
    run_command('/usr/bin/docker-compose --file /root/gitSwarm/dbcm-base-managers/compose/mysql.yml --project-name mysqlms832  scale mysql=2')


if __name__ == '__main__':
    t1()
