from linked_list import *


def get_list():
    n = Node(-1)
    add(n, Node(1))
    add(n, Node(2))
    add(n, Node(3))
    add(n, Node(4))
    add(n, Node(5))
    return n


def reverse1():
    l = get_list()
    print(string(l))
    if l.next is None or l.next.next is None:
        print(string(l))
        return
    pre = l.next
    tmp = pre.next
    pre.next = None
    while tmp is not None:
        next = tmp.next
        tmp.next = pre
        pre = tmp
        tmp = next
    l.next = pre
    print(string(l))


if __name__ == '__main__':
    reverse1()
