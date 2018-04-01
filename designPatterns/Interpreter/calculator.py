from expression import VarExpression, AddExpression, SubExpression


class Calculator(object):

    def __init__(self, exp_str):
        stack = []
        l = len(exp_str)
        i = 0
        while i < l:
            if exp_str[i] == '+':
                left = stack.pop()
                right = VarExpression(exp_str[i+1])
                i += 1
                stack.append(AddExpression(left, right))
            elif exp_str[i] == '-':
                left = stack.pop()
                right = VarExpression(exp_str[i+1])
                i += 1
                stack.append(SubExpression(left, right))
            else:
                stack.append(VarExpression(exp_str[i]))
            i += 1
        self._expression = stack.pop()

    def run(self, var):
        return self._expression.interpreter(var)
