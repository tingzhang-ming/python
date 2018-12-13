import threading
import random
import time

global count, event1, event2, event3

count = 0
event1 = threading.Event()
event2 = threading.Event()
event3 = threading.Event()

event1.clear()
event2.clear()
event3.clear()


def print_str(s):
    print s
    a = random.randint(1, 100)/100.0
    time.sleep(a)


class ThreadA(threading.Thread):

    def run(self):
        global lock, count, event1, event2, event3
        for i in range(10):
            while count % 3 != 0:
                event1.wait()
                event1.clear()
            print_str("A")
            count += 1
            event2.set()


class ThreadB(threading.Thread):

    def run(self):
        global count, event1, event2, event3
        for i in range(10):
            while count % 3 != 1:
                # print event2.is_set()
                event2.wait()
                event2.clear()
            print_str("B")
            count += 1
            event3.set()


class ThreadC(threading.Thread):

    def run(self):
        global count, event1, event2, event3
        for i in range(10):
            while count % 3 != 2:
                event3.wait()
                event3.clear()
            print_str("C")
            count += 1
            event1.set()


if __name__ == '__main__':
    ThreadA().start()
    ThreadB().start()
    ThreadC().start()
