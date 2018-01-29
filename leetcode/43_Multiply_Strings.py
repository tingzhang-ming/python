"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

    The length of both num1 and num2 is < 110.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = len(num1)
        n2 = len(num2)
        tmpres = [0] * (n1 + n2)
        k = n1 + n2 - 2
        for i in range(n1):
            for j in range(n2):
                tmpres[k - i - j] += int(num1[i]) * int(num2[j])
        carry = 0
        for i in range(n1 + n2):
            tmpres[i] += carry
            carry = tmpres[i] / 10
            tmpres[i] %= 10
        i = k + 1
        while i >= 0 and tmpres[i] == 0:
            i -= 1
        if i < 0:
            return '0'
        return ''.join([str(tmpres[ss]) for ss in range(i, -1, -1)])


if __name__ == '__main__':
    s = Solution()
    print s.multiply('1', '1')
