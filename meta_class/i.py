from abc import ABCMeta, abstractmethod


class Meta(ABCMeta):

    def __call__(self, *args, **kwargs):
        instance = super(Meta, self).__call__(*args, **kwargs)
        if not hasattr(instance, "_level") or not instance._level:
            raise Exception("Handler object's _level must be set a valid value.")
        return instance


class BaseHandler(object):

    __metaclass__ = Meta

    @abstractmethod
    def __init__(self, level):
        self._level = level

    def get_level(self):
        print self._level


class Handler(BaseHandler):

    def __init__(self):
        super(Handler, self).__init__(2)

    def a(self):
        pass

if __name__ == '__main__':
    h = Handler()
    h.get_level()

