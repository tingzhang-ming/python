"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not haystack and not needle:
            return 0
        if not haystack:
            return -1
        if not needle:
            return 0
        l = len(haystack)
        l2 = len(needle)
        for i in range(l):
            if haystack[i] == needle[0] and i + l2 <= l:
                has = True
                for j in range(l2):
                    if haystack[i+j] != needle[j]:
                        has = False
                        break
                if has:
                    return i
        return -1
