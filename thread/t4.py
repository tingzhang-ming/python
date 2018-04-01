from threading import Thread, Event
import time


def work(event):
    print "work start------------"
    while event.wait():
        print "d in work-----------"
        time.sleep(10)
        print "work done, continue wait"
        event.clear()


def t1():
    event = Event()
    Thread(target=work, args=(event,)).start()
    event.set()

if __name__ == '__main__':
    # t1()
    print time.time() - 1522336508
