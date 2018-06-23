from linked_list import *


def get_list():
    n = Node(-1)
    add(n, Node(1))
    add(n, Node(2))
    add(n, Node(3))
    n4 = add(n, Node(4))
    add(n, Node(5))
    last = add(n, Node(6))
    return n, last


# O(1)
def delete_one():
    l, d = get_list()
    if l is None or d is None or l.next is None:
        print("nothing to do")
        return
    if d.next is not None:
        d.data = d.next.data
        d.next = d.next.next
    else:
        pre = l
        while pre.next.next is not None:
            pre = pre.next
        pre.next = pre.next.next
    print(string(l))


if __name__ == '__main__':
    delete_one()
