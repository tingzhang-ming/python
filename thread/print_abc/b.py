import random
import time
import threading

global lock, count

lock = threading.Lock()
count = 0


def print_str(s):
    print s
    a = random.randint(1, 100)/100.0
    time.sleep(a)


class ThreadA(threading.Thread):

    def run(self):
        global lock, count
        i=0
        while i < 10:
            with lock:
                if count % 3 == 0:
                    print_str("A")
                    count += 1
                    i += 1


class ThreadB(threading.Thread):

    def run(self):
        global lock, count
        i=0
        while i < 10:
            with lock:
                if count % 3 == 1:
                    print_str("B")
                    count += 1
                    i += 1


class ThreadC(threading.Thread):

    def run(self):
        global lock, count
        i=0
        while i < 10:
            with lock:
                if count % 3 == 2:
                    print_str("C")
                    count += 1
                    i += 1


if __name__ == '__main__':
    ThreadA().start()
    ThreadB().start()
    ThreadC().start()
