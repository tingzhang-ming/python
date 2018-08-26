
"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l_s = len(s)
        dp = [[False] * l_s for _ in range(l_s)]
        l = 0
        r = 0
        max_v = 0
        for j in range(l_s):
            dp[j][j] = True
            for i in range(j):
                if j == i+1 and s[i] == s[j]:
                    dp[i][j] = True
                if j > i+1:
                    dp[i][j] = (dp[i+1][j-1] and (s[i] == s[j]))
                if dp[i][j] and max_v < j-i+1:
                    max_v = j-i+1
                    l = i
                    r = j
        return s[l:r+1]


if __name__ == '__main__':
    s = Solution()
    print s.longestPalindrome("cbbd")
