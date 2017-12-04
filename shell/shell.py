import subprocess
import sys
import time


def run_shell(cmd):
    proc = subprocess.Popen(args=cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    proc.wait()
    output = proc.stdout.read()
    error = proc.stderr.read()
    return output.strip(), error.strip()


def run_shell2(cmd):
    proc = subprocess.Popen(args=cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    print "---------------------"
    for line in iter(proc.stdout.readline, 'b'):
        line = line.strip('\r\n')
        print line


def t1():
    cmd = "mysqldump -uroot -proot.123 -h109.105.4.65 -P32770 " \
          "mhc2 runoob_tbl4 runoob_tbl3  --set-gtid-purged=OFF --opt | gzip  " \
          ">  /root/test/dump/test1_mhc2_multi.dump.gz"
    output, err = run_shell(cmd)
    print "output-------------"
    print output
    print "error--------------"
    print err
    print "--------------------"
    result = ""
    if err is not "":
        for e in err.split("\n"):
            if e.startswith("mysqldump:"):
                result += e.split("mysqldump:")[1].strip() + '\n'
            if e.startswith("ERROR"):
                result += e + '\n'
    print result


def t2():
    cmd = "gunzip <  /root/test/dump/test1_mhc2_multi.dump.gz | " \
          "mysql -uroot -proot.123 -h109.105.4.65 -P32773 mhc2"
    output, error = run_shell(cmd)
    print "output-------------"
    print output
    print "error--------------"
    print error
    print "--------------------"
    result = ""
    if error is not "":
        for e in error.split("\n"):
            if e.startswith("mysqldump:"):
                result += e.split("mysqldump:")[1].strip() + '\n'
            if e.startswith("ERROR"):
                result += e
    print result.strip()


def t3():
    cmd = "mysqldump -uroot -proot.123 -h109.105.4.65 -P32770 " \
          "mhc3  --set-gtid-purged=OFF --opt | gzip  " \
          ">  /root/test/dump/test1_mhc2_multi.dump.gz"
    output, err = run_shell(cmd)
    print "output-------------"
    print output
    print "error--------------"
    print err
    print "--------------------"
    result = ""
    if err is not "":
        for e in err.split("\n"):
            if e.startswith("mysqldump:"):
                result += e.split("mysqldump:")[1].strip() + '\n'
            if e.startswith("ERROR"):
                result += e + '\n'
    print result


def t4():
    cmd = "pv /root/test/dump/test1.dump | mysql -uroot -proot.123 -h109.105.4.65 -P32776"
    run_shell2(cmd)

if __name__ == '__main__':
    print 2 ** 16
