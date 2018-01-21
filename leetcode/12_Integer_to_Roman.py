# encoding: utf-8
"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
I = 1;
V = 5;
X = 10;
L = 50;
C = 100;
D = 500;
M = 1000;
"""


class Solution(object):

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        n = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        res = ""
        for i in range(len(s)):
            if num == 0:
                break
            while num >= n[i]:
                res += s[i]
                num -= n[i]
        return res


if __name__ == '__main__':
    s = Solution()
    print s.intToRoman(1900)
