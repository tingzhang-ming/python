# encoding: utf-8
"""
Divide two integers without using multiplication, division and mod(取余) operator.

If it is overflow, return MAX_INT.
"""


class Solution(object):

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return 2147483647
        yihao = False
        if (divisor > 0 and dividend < 0) or (divisor < 0 and dividend > 0):
            yihao = True
        res = 0
        if divisor < 0:
            divisor = -divisor
        if dividend < 0:
            dividend = -dividend
        while dividend >= divisor:
            t = divisor
            count = 1
            while t + t <= dividend:
                t += t
                count += count
            res += count
            dividend -= t
        if yihao:
            if res > 2147483648:
                res = 2147483648
            return -res
        if res > 2147483647:
            res = 2147483647
        return res

    def divide2(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return 2147483647
        yihao = False
        if (divisor > 0 and dividend < 0) or (divisor < 0 and dividend > 0):
            yihao = True
        res = 0
        if divisor < 0:
            divisor = -divisor
        if dividend < 0:
            dividend = -dividend
        while dividend >= divisor:
            t = divisor
            p = 1
            while dividend > (t << 1):
                t <<= 1
                p <<= 1
            res += p
            dividend -= t
        if yihao:
            if res > 2147483648:
                res = 2147483648
            return -res
        if res > 2147483647:
            res = 2147483647
        return res
