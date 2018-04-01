# encoding: utf-8
from calculator import Calculator


def get_exp_str():
    return raw_input("请输入表达式:")


def get_value(exp_str):
    m = {}
    for i in exp_str:
        if i != '+' and i != '-':
            if i not in m:
                m[i] = int(raw_input("输入%s的值:" % i))
    return m


def main():
    exp_str = get_exp_str()
    var = get_value(exp_str)
    cal = Calculator(exp_str)
    print "运算结果为: ", exp_str, "=", cal.run(var)


if __name__ == '__main__':
    main()

# 请输入表达式:a+b-c
# 输入a的值:100
# 输入b的值:20
# 输入c的值:40
# 运算结果为:  a+b-c = 80