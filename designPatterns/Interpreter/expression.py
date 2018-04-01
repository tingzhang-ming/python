from abc import ABCMeta, abstractmethod


class AbstractExpression(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def interpreter(self, var):
        pass


class VarExpression(AbstractExpression):

    def __init__(self, key):
        self._key = key

    def interpreter(self, var):
        return var[self._key]


class AbstractSymbolExpression(AbstractExpression):

    __metaclass__ = type(AbstractExpression)

    def __init__(self, left, right):
        self._left = left
        self._right = right

    @abstractmethod
    def interpreter(self, var):
        pass


class AddExpression(AbstractSymbolExpression):

    def __init__(self, left, right):
        super(AddExpression, self).__init__(left, right)

    def interpreter(self, var):
        return self._left.interpreter(var) + self._right.interpreter(var)


class SubExpression(AbstractSymbolExpression):
    def __init__(self, left, right):
        super(SubExpression, self).__init__(left, right)

    def interpreter(self, var):
        return self._left.interpreter(var) - self._right.interpreter(var)
