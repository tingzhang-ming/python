from strategies.app1 import get_app1_strategy
from other.app3 import get_app3_strategy


def t1():
    app_class = get_app1_strategy('imp1.Imp1')
    app = app_class()
    app.m1()
    app.m2()


def t2():
    app_class = get_app3_strategy('imp1.Imp1')
    app = app_class()
    app.m1()
    app.m2()


if __name__ == '__main__':
    t2()
