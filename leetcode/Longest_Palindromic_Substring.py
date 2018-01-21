# encoding: utf-8
"""
Given a string s, find the longest palindromic(回文) substring in s. 
You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
"""

"""
d(i, j) = True      if s[i]...s[j] is a palindromic
        = False     otherwise

d(i, j) = d(i+1, j-1) and s[i] == s[j]
d(i, i) = True
d(i, i+1) = (s[i]==s[i+1])
"""


class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        start = end = 0
        for i in range(l):
            len1 = self.expand_around_center(s, i, i)
            len2 = self.expand_around_center(s, i, i+1)
            mlen = max(len1, len2)
            if mlen > end - start:
                start = i - (mlen - 1)/2
                end = i + mlen/2
        return s[start:end+1]

    def expand_around_center(self, s, left, right):
        l = left
        r = right
        sl = len(s)
        while l >= 0 and r < sl and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1


    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        d = [[False] * l for _ in range(l)]
        cha = 0
        start = end = 0
        for i in range(l):
            d[i][i] = True
            if i+1 < l:
                d[i][i + 1] = s[i] == s[i + 1]
        for i in range(l):
            for k in range(l):
                if i+k+1 < l and i-k-1 > 0:
                    d[i+k][i-k] = d[i+k+1][i-k-1] and s[i+k][i-k]
                if i + k + 1 < l and i - k > 0:
                    d[i + k][i + 1 - k] = d[i + k + 1][i - k] and s[i + k][i + 1 - k]

        for i in range(l):
            for j in range(l):
                if d[i][j] and j-i > cha:
                    cha = j - i
                    start = i
                    end = j
        print_d(d)
        return s[start:end+1]


def print_d(d):
    for i in d:
        print i

a = "jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel"
b = "abcba"

if __name__ == '__main__':
    s = Solution()
    print s.longestPalindrome(b)
