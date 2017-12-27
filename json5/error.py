import json

path = '/root/github/python/json5/test.json'


def t1():
    try:
        a = json.load(open(path))
        print a
    except IOError as e:
        print str(e)        # [Errno 2] No such file or directory: '/root/github/python/json5/test.jsons'
                            # [Errno 21] Is a directory: '/root/github/python/json5'
    except ValueError as e:
        print 'Parse json failed: %s' % str(e)



if __name__ == '__main__':
    t1()
