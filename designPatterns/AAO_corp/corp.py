# encoding: utf-8


class Corp(object):

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        self.parent = None

    def get_info(self):
        return "name: {}, position: {}, salary: {}".format(self.name, self.position, self.salary)


class Leaf(Corp):

    def __init__(self, name, position, salary):
        super(Leaf, self).__init__(name, position, salary)


class Branch(Corp):
    def __init__(self, name, position, salary):
        super(Branch, self).__init__(name, position, salary)
        self.subordinate_list = []

    def add_subordinate(self, corp):
        corp.parent = self
        self.subordinate_list.append(corp)

###############################################################################


def composite_corp_tree():
    ceo = Branch("王大麻子", "总经理", 100000)

    develop_dep = Branch("刘大瘸子", "研发部门经理", 20000)
    sales_dep = Branch("马二拐子", "销售部门经理", 20000)
    finance_dep = Branch("赵三坨子", "财务部经理", 30000)

    first_dev_group = Branch("杨三奥迪", "开发一组组长", 5000)
    second_dev_group = Branch("吴大棒槌", "开发二组组长", 6000)

    a = Leaf("a", "研发人员", 2000)
    b = Leaf("b", "研发人员", 2000)
    c = Leaf("c", "研发人员", 2000)
    d = Leaf("d", "研发人员", 2000)
    e = Leaf("e", "研发人员", 2000)
    f = Leaf("f", "研发人员", 2000)
    h = Leaf("h", "销售人员", 2000)
    i = Leaf("i", "销售人员", 2000)
    j = Leaf("j", "财务人员", 2000)
    k = Leaf("k", "ceo秘书", 2000)
    zhengLaoLiu = Leaf("郑老六", "研发部副总", 2000)

    ceo.add_subordinate(develop_dep)
    ceo.add_subordinate(sales_dep)
    ceo.add_subordinate(finance_dep)
    ceo.add_subordinate(k)

    develop_dep.add_subordinate(first_dev_group)
    develop_dep.add_subordinate(second_dev_group)
    develop_dep.add_subordinate(zhengLaoLiu)

    first_dev_group.add_subordinate(a)
    first_dev_group.add_subordinate(b)
    first_dev_group.add_subordinate(c)
    second_dev_group.add_subordinate(d)
    second_dev_group.add_subordinate(e)
    second_dev_group.add_subordinate(f)

    sales_dep.add_subordinate(h)
    sales_dep.add_subordinate(i)
    finance_dep.add_subordinate(j)
    return ceo


def get_tree_info(root):
    info = ""
    for s in root.subordinate_list:
        if isinstance(s, Leaf):
            info = info + s.get_info() + "\n"
        else:
            info = info + s.get_info() + "\n" + get_tree_info(s)
    return info


if __name__ == '__main__':
    ceo = composite_corp_tree()
    print(ceo.get_info())
    print(get_tree_info(ceo))
# name: 王大麻子, position: 总经理, salary: 100000
# name: 刘大瘸子, position: 研发部门经理, salary: 20000
# name: 杨三奥迪, position: 开发一组组长, salary: 5000
# name: a, position: 研发人员, salary: 2000
# name: b, position: 研发人员, salary: 2000
# name: c, position: 研发人员, salary: 2000
# name: 吴大棒槌, position: 开发二组组长, salary: 6000
# name: d, position: 研发人员, salary: 2000
# name: e, position: 研发人员, salary: 2000
# name: f, position: 研发人员, salary: 2000
# name: 郑老六, position: 研发部副总, salary: 2000
# name: 马二拐子, position: 销售部门经理, salary: 20000
# name: h, position: 销售人员, salary: 2000
# name: i, position: 销售人员, salary: 2000
# name: 赵三坨子, position: 财务部经理, salary: 30000
# name: j, position: 财务人员, salary: 2000
# name: k, position: ceo秘书, salary: 2000