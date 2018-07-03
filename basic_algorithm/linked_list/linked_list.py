

class Node(object):
    def __init__(self, data, node=None):
        self.data = data
        self.next = node


def length(head):
    p = head.next
    l = 0
    while p:
        l += 1
        p = p.next
    return l


def string(head):
    res = '['
    p = head.next
    while p:
        res += str(p.data)
        if p.next:
            res += ', '
        p = p.next
    res += ']'
    return res


def add(head, node):
    p = q = head
    while p:
        q = p
        p = p.next
    q.next = node
    node.next = None
    return node


def add_index(head, index, node):
    l = length(head)
    if index > l:
        return False
    p = head
    for i in range(index):
        p = p.next
    node.next = p.next
    p.next = node
    return True


def delete(head, index):
    l = length(head)
    if index > l:
        return False
    p = q = head
    for i in range(index):
        q = p
        p = p.next
    q.next = p.next
    return True


def reverse(head):
    current = head.next
    while current.next is not None:
        p = current.next
        current.next = p.next
        p.next = head.next
        head.next = p


if __name__ == '__main__':
    ll = Node(-1)
    add(ll, Node(1))
    add(ll, Node(2))
    add(ll, Node(3))
    add(ll, Node(4))
    add(ll, Node(5))
    print length(ll)
    print string(ll)
    add_index(ll, 1, Node(999))
    print string(ll)
    add_index(ll, 0, Node(888))
    print string(ll)
    add_index(ll, 7, Node(777))
    print string(ll)
    add_index(ll, 11, Node(777))
    print string(ll)
    delete(ll, 1)
    print string(ll)
    delete(ll, 7)
    print string(ll)
    delete(ll, 2)
    print string(ll)
    reverse(ll)
    print string(ll)

