# encoding: utf-8
# 函数运行的时候启动线程, 函数结束的时候关闭线程

import threading
import time


def main(a=0):
    def t(event):
        while not event.is_set():
            print "thread run..."
            time.sleep(1)
        print "thread exit"

    event = None
    if a == 1:
        event = threading.Event()
        t = threading.Thread(target=t, args=(event,))
        t.start()
    time_o = 10
    while time_o > 0:
        print "main run..."
        time.sleep(1)
        time_o -= 1
    if event:
        event.set()

if __name__ == "__main__":
    main(1)

