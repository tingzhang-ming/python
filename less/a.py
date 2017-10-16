import sys
import subprocess

def pager_pipe(text, cmd):
    ''' pipe text through a pager '''
    try:
        cmd = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=sys.stdout)
        cmd.communicate(input=str(text))
    except IOError:
        pass
    except KeyboardInterrupt:
        pass

def t1():
    text = "sdfsdfdfsdf fsdfasdfasd ffsdfsdaf "
    pager_pipe(text, "less")

def t2():
    text = "sdfsdfdfsdf fsdfasdfasd ffsdfsdaf \n hahah \n sdfsdfdsfggggg"
    pager_pipe(text, "grep haha")
    print "hahahah"

if __name__ == '__main__':
    t2()