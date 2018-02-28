# encoding: utf-8

def t1():
    students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
    print sorted(students, key=lambda student: student[2])
    # students.sort()
    # print students


def t11():
    students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
    students.sort(key=lambda student: student[2])
    print students


def cmp(x, y):
    lx = len(x)
    ly = len(y)
    if lx < ly:
        return -1
    if lx > ly:
        return 1
    return 0


def t2():
    students = [('john', 'A', 15), ('jane', 'BB7777', 12), ('dave', 'BCC', 10)]
    print sorted(students, cmp=cmp, key=lambda student: student[1])


"""
alist = [('2', '3', '10'), ('1', '2', '3'), ('5', '6', '7'), ('2', '5', '10'), ('2', '4', '10')]
# 多级排序，先按照第3个元素排序，然后按照第2个元素排序：
print sorted(alist, cmp=None, key=lambda x: (int(x[2]), int(x[1])), reverse=False)
-------------------------------------------------------------------------------------------
[('1', '2', '3'), ('5', '6', '7'), ('2', '3', '10'), ('2', '4', '10'), ('2', '5', '10')]
"""

if __name__ == '__main__':
    t2()
