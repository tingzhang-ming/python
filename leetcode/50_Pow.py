"""
Implement pow(x, n).

Example 1:

Input: 2.00000, 10
Output: 1024.00000

Example 2:

Input: 2.10000, 3
Output: 9.26100
"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1 / self.power(x, -n)
        return self.power(x, n)

    def power(self, x, n):
        if n == 0:
            return 1
        half = self.power(x, n/2)
        if n % 2 == 0:
            return half * half
        return x * half * half


if __name__ == '__main__':
    s = Solution()
    print s.myPow(2.00000, -2147483648)
