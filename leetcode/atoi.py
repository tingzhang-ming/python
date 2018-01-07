"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases.
If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
You are responsible to gather all the input requirements up front.
"""


class Solution(object):

    def get_start(self, str, l):
        i = -1
        for i in range(l):
            if not (str[i] == ' ' or str[i] == '0'):
                break
        return i

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        l = len(str)
        start = self.get_start(str, l)
        if start == -1:
            return 0
        fu = False
        if str[start] == '-':
            fu = True
            start += 1
        elif str[start] == '+':
            fu = False
            start += 1
        res = ''
        for i in xrange(l-start+1):
            try:
                num = int(str[i+start])
                res += str[i+start]
            except:
                break
        if not res:
            return 0
        res = int(res)
        if fu:
            if res > 2147483648:
                res = 2147483648
            return res * -1
        if res > 2147483647:
            res = 2147483647
        return res


if __name__ == '__main__':
    s = Solution()
    print s.myAtoi("2147483648")
