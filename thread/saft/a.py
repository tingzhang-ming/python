import time
from threading import Thread

l = [0, 1, 2, 3]


def ap():
    for _ in range(100):
        time.sleep(0.1)
        l[0] += 1


if __name__ == '__main__':
    for i in range(5):
        Thread(target=ap).start()
    time.sleep(15)
    print l

# [497, 1, 2, 3]
