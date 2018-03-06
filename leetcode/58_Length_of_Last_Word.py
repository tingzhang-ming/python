"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""


class Solution(object):

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        l = len(s)
        if l == 0:
            return 0
        res = 0
        for i in range(l-1, -1, -1):
            if s[i] == ' ':
                break
            res += 1
        return res

    def lengthOfLastWord3(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        l = len(s)
        if l == 0:
            return 0
        index = -1
        for i in range(l):
            if s[i] == ' ':
                index = i
        if index == -1:
            return l
        return l-index



    def lengthOfLastWord2(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss = s.split()
        if len(ss) == 0:
            return 0
        return len(ss[-1])
