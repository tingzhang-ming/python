

class Enum(set):
  def __getattr__(self, name):
    if name in self:
      return name
    raise AttributeError("{} not in enum({})".format(name, ", ".join(list(self))))


ACTIONS = Enum(['buy_computer',
                'sell_computer',
                'off_sell',
                'clear_stock'])
