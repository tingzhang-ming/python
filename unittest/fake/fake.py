

class Fake(object):
    def __init__(self):
        pass

    def __getitem__(self, k):
        # fake object can used as dict: fake["key"]
        if isinstance(k, str):
            return self.__dict__.get(k)
        # fake object can used as list: fake[0], fake[1], ...
        if not self.__dicts__:
            self.__dicts__ = self.to_dict()
        if not self.__lists__:
            self.__lists__ = []
            for key, val in self.__dicts__.items():
                self.__lists__.append(val)
        return self.__lists__[k]

    def __setitem__(self, k, v):
        self.__dict__[k] = v

    def __getattr__(self, k):
        return self.__dict__.get(k)

    def to_dict(self):
        d = {}
        for k in dir(self):
            v = getattr(self, k)
            if not k.startswith("__") and not callable(v):
                d[k] = v
        return d
