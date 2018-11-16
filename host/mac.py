import uuid


def t1():
    mac = uuid.getnode()
    print type(mac)
    print mac


if __name__ == '__main__':
    t1()
