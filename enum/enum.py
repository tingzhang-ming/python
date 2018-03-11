

class Enum(set):
  def __getattr__(self, name):
    if name in self:
      return name
    raise AttributeError("{} not in enum({})".format(name, ", ".join(list(self))))


if __name__ == '__main__':
    a = Enum(["haha", "lala"])
    print a.haha
    print a.kkk

