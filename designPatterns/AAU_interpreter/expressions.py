from abc import ABCMeta, abstractmethod


class Expression(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def interpreter(self, var):
        pass


class VarExpression(Expression):

    def __init__(self, key):
        self.key = key

    def interpreter(self, var):
        return var.get(self.key, None)


class SymbolExpression(Expression):

    __metaclass__ = ABCMeta

    def __init__(self, left, right):
        self.left = left
        self.right = right


class AddExpression(SymbolExpression):

    def __init__(self, left, right):
        super(AddExpression, self).__init__(left, right)

    def interpreter(self, var):
        return self.left.interpreter(var) + self.right.interpreter(var)


class SubExpression(SymbolExpression):

    def __init__(self, left, right):
        super(SubExpression, self).__init__(left, right)

    def interpreter(self, var):
        return self.left.interpreter(var) - self.right.interpreter(var)


