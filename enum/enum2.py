

class EnumLevel(dict):
  def __getattr__(self, name):
    if name in self:
      return self[name]
    raise AttributeError("{} not in enum({})".format(name, ", ".join(list(self))))


if __name__ == '__main__':
    a = EnumLevel({"aa": 1, "bb": 2})
    print a.aa
    print a.bb

