"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
"""


class Solution(object):

    def update_res(self, res, stack):
        stack_reverse = [i for i in reversed(stack)]
        if stack == stack_reverse:
            res = [i for i in stack]
        return res

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        res = []
        l = len(s)
        res_s = ""
        for i in xrange(l):
            for j in xrange(i, l):
                stack.append(s[j])
                res = self.update_res(res, stack)
            del stack[:]
            if len(res) > len(res_s):
                res_s = ""
                for i in res:
                    res_s += i
        return res_s

a = "jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel"

if __name__ == '__main__':
    s = Solution()
    print s.longestPalindrome(a)
