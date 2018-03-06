from functools import wraps
import threading

_singleton_lock = threading.Lock()


def singleton(cls):
    instances = {}

    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            with _singleton_lock:
                if cls not in instances:
                    instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance


@singleton
class Emperor(object):

    def __init__(self):
        print 'emperor __init__'
        self.name = None

    def say(self):
        print "my name: %s" % self.name

