import threading


class Singleton(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        cls._lock = threading.Lock()
        super(Singleton, cls).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls._lock:
                if cls.__instance is None:
                    cls.__instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instance


class Singleton2(type):
    __instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singleton2, cls).__call__(*args, **kwargs)
        return cls.__instance


class Emperor(object):

    __metaclass__ = Singleton2

    def __init__(self):
        print('emperor __init__')
        self.name = None

    def say(self):
        print("my name: %s" % self.name)

