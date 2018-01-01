

class Node(object):

    def __init__(self, data, lnode=None, rnode=None):
        self.data = data
        self.lnode = lnode
        self.rnode = rnode


def add(node, *args):
    l = len(args)
    if l > 0:
        node.lnode = Node(args[0])
    if l > 1:
        node.rnode = Node(args[1])


def pre_order(root):
    p = root
    stack = []
    res = []
    while p is not None or len(stack) > 0:
        while p is not None:
            res.append(p.data)
            stack.append(p)
            p = p.lnode
        if len(stack) > 0:
            p = stack.pop()
            p = p.rnode
    return res


def in_order(root):
    p = root
    stack = []
    res = []
    while p is not None or len(stack) > 0:
        while p is not None:
            stack.append(p)
            p = p.lnode
        if len(stack) > 0:
            p = stack.pop()
            res.append(p.data)
            p = p.rnode
    return res


def post_order(root):
    p = root
    stack = []
    flag_stack = []
    res = []
    while p is not None or len(stack) > 0:
        while p is not None:
            stack.append(p)
            flag_stack.append(False)
            p = p.lnode
        while 1:
            if len(stack) > 0 and flag_stack[-1] == True:
                v = stack.pop()
                flag_stack.pop()
                res.append(v.data)
            else:
                break
        if len(stack) > 0:
            p = stack[-1].rnode
            flag_stack[-1] = True
    return res


if __name__ == '__main__':
    bt = Node(1)
    add(bt, 2, 3)
    add(bt.lnode, 4, 5)
    add(bt.rnode, 6, 7)
    print pre_order(bt)
    print in_order(bt)
    print post_order(bt)
