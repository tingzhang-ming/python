# encoding: utf-8
"""
Write a function to find the longest common prefix string amongst an array of strings. 
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        a = strs[len(strs)-1]
        res = ""

        for i in range(len(a)):
            end = False
            for s in strs:
                if i >= len(s) or a[i] != s[i]:
                    end = True
            if end:
                break
            else:
                res += a[i]
        return res
