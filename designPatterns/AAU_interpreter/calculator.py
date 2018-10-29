from expressions import VarExpression, AddExpression, SubExpression


class Calculator(object):

    def __init__(self, exp_str):
        stack = []
        i = 0
        while i < len(exp_str):
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
        self.expression = stack.pop()

    def run(self, var):
        return self.expression.interpreter(var)
