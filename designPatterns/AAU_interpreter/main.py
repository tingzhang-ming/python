# encoding: utf-8
from calculator import Calculator


def main():
    exp_str = get_exp_str()
    var = get_value(exp_str)
    cal = Calculator(exp_str)
    print "运算结果: " + exp_str + "=" + str(cal.run(var))


def get_exp_str():
    print "请输入表达式:"
    return raw_input()


def get_value(exp_str):
    res = {}
    for ch in exp_str:
        if ch != '+' and ch != '-':
            if ch not in res:
                print "输入" + ch + "的值:"
                i = raw_input()
                res[ch] = int(i)
    return res


if __name__ == '__main__':
    main()
