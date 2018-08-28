from abc import ABCMeta, abstractmethod


class Meta(ABCMeta):

    def __call__(cls, *args, **kwargs):
        instance = super(Meta, cls).__call__(*args, **kwargs)
        if not hasattr(instance, "_level") or not instance._level:
            raise Exception("Handler object's _level must be set a valid value.")
        return instance


class EnumLevel(dict):
  def __getattr__(self, name):
    if name in self:
      return self[name]
    raise AttributeError("{} not in enum({})".format(name, ", ".join(list(self))))


LEVELS = EnumLevel({"father": 1, "husband": 2, "son": 3})


class Handler(object):

    __metaclass__ = Meta

    @abstractmethod
    def __init__(self, level):
        self._level = level
        self._next_handler = None

    @abstractmethod
    def response(self, women):
        pass

    def handle_message(self, women):
        self.response(women)

    def handles(self, women):
        return women.get_type() == self._level
