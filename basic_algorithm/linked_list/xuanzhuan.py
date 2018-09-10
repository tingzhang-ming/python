from linked_list import *


def get_list():
    n = Node(-1)
    add(n, Node(1))
    add(n, Node(2))
    add(n, Node(3))
    add(n, Node(4))
    add(n, Node(5))
    add(n, Node(6))
    return n


def xuanzhuan():
    l = get_list()
    n = 3
    print(string(l))
    p = l.next
    pre = p
    while n > 0:
        pre = p
        p = p.next
        n -= 1
    tmp = p
    while p.next is not None:
        p = p.next
    p.next = l.next
    l.next = tmp
    pre.next = None
    print(string(l))

if __name__ == '__main__':
    xuanzhuan()
