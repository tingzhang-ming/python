from linked_list import *


def get_list():
    n = Node(-1)
    add(n, Node(1))
    add(n, Node(2))
    add(n, Node(3))
    n4 = add(n, Node(4))
    add(n, Node(5))
    last = add(n, Node(6))
    last.next = n4
    return n


def get_huan():
    l = get_list()
    slow = l
    fast = l
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            slow = l
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow.data
    return 0


if __name__ == '__main__':
    res = get_huan()
    if res > 0:
        print("you huan")
        print res
    else:
        print("mei you")
