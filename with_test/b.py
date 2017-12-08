

class ValueErrorSubclass(ValueError):
    pass


class HandleValueError(object):

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_type:
            return True
        if exc_type == ValueError:
            print 'Handling ValueError: %s' % exc_val
            return True
        return False


if __name__ == '__main__':
    with HandleValueError():
        raise ValueError('foo bar baz')
    print '-------------------------------------'
    with HandleValueError():
        raise ValueErrorSubclass('foo bar baz')

# Handling ValueError: foo bar baz
# -------------------------------------
# Traceback (most recent call last):
#   File "/root/github/python/with_test/b.py", line 26, in <module>
#     raise ValueErrorSubclass('foo bar baz')
# __main__.ValueErrorSubclass: foo bar baz
