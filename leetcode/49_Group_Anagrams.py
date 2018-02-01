"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note: All inputs will be in lower-case.
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        tmp = {}
        for s in strs:
            tmp_s = [si for si in s]
            tmp_s.sort()
            new_str = ''.join(tmp_s)
            if new_str not in tmp:
                tmp[new_str] = [s]
            else:
                tmp[new_str].append(s)
        return tmp.values()
