import sys
import signal
import time


def worker():
    while True:
        print 'do something'
        time.sleep(2)


def myHandler(signum, frame):
    print('I received: ', signum)
    print 'I will exit'
    sys.exit(0)

# register signal.SIGTSTP's handler
signal.signal(signal.SIGTERM, myHandler)
worker()
print('End of Signal Demo')

