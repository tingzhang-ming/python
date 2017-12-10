from registry import Registry

a = Registry()
b = Registry()

@a.register
def foo(x=3):
    return x

@b.register
def bar(x=5):
    return x

@a.register
@b.register
def bar(x=7):
    return x

if __name__ == '__main__':
    print a.run_all()
    print b.run_all()
    # [3, 7]
    # [5, 7]
    print a.run_all(x=10)
    #[10, 10]