#encoding: utf-8
#一个函数和它的环境变量合在一起，就构成了一个闭包(closure)

def line_conf(a, b):
    def line(x):
        return a * x + b
    return line

if __name__ == '__main__':
    myline1 = line_conf(1,2)
    myline2 = line_conf(2,4)

    print myline1(2)
    print myline2(2)

# 4
# 8