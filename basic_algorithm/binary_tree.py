

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


def post_order(p):
    stack = []
    flag_stack = []
    res = []
    while p is not None or len(stack) > 0:
        while p is not None:
            stack.append(p)
            flag_stack.append(False)
            p = p.lnode
        while len(stack) > 0 and flag_stack[-1] is True:
            v = stack.pop()
            flag_stack.pop()
            res.append(v.data)
        if len(stack) > 0:
            p = stack[-1].rnode
            flag_stack[-1] = True
    return res


def pre_order2(root):
    res = []
    pre_dfs(root, res)
    return res


def pre_dfs(p, res):
    res.append(p.data)
    if p.lnode:
        pre_dfs(p.lnode, res)
    if p.rnode:
        pre_dfs(p.rnode, res)


def in_order2(root):
    res = []
    in_dfs(root, res)
    return res


def in_dfs(p, res):
    if p.lnode:
        in_dfs(p.lnode, res)
    res.append(p.data)
    if p.rnode:
        in_dfs(p.rnode, res)


def post_order2(root):
    res = []
    post_dfs(root, res)
    return res


def post_dfs(p, res):
    if p.lnode:
        post_dfs(p.lnode, res)
    if p.rnode:
        post_dfs(p.rnode, res)
    res.append(p.data)


if __name__ == '__main__':
    bt = Node(1)
    add(bt, 2, 3)
    add(bt.lnode, 4, 5)
    add(bt.rnode, 6, 7)
    print(pre_order2(bt))
    print(in_order2(bt))
    print(post_order2(bt))
