# encoding: utf-8
"""
Given a roman numeral, convert it to an integer.

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
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = dict(
            I=1,
            V=5,
            X=10,
            L=50,
            C=100,
            D=500,
            M=1000,
        )
        res = 0
        for i in range(len(s)):
            res += m[s[i]]
            if i >= 1 and m[s[i]] > m[s[i-1]]:
                res -= 2 * m[s[i-1]]
        return res