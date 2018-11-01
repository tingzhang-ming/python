from io import BytesIO as StringIO


def t1():
    f = StringIO()
    f.write('hello')
    f.write(' ')
    f.write('world')
    print f.getvalue()
    f.close()


if __name__ == '__main__':
    t1()
