"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"

Example 2:

Input: 4
Output: "1211"
"""


class Solution(object):

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if not n:
            return ''
        shang = '1'
        for _ in range(1, n):
            l = len(shang)
            res = ''
            count = 1
            for i in range(1, l):
                if shang[i] == shang[i-1]:
                    count += 1
                else:
                    res += str(count) + shang[i-1]
                    count = 1
            res += str(count) + shang[-1]
            shang = res
        return shang

    def get(self, s, x, l):
        count = 1
        for i in range(x+1, l):
            if s[i] == s[x]:
                count += 1
                continue
            else:
                break

        return '{}{}'.format(str(count), s[x]), x + count

    def countAndSay2(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        shang = '1'
        for i in range(1, n):
            end = 0
            l = len(shang)
            res = ''
            while end < l:
                ss, end = self.get(shang, end, l)
                res += ss
            shang = res
        return shang


if __name__ == '__main__':
    s = Solution()
    print s.countAndSay(4)
