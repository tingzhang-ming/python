"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want. 
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        m = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []
        self.dfs(digits, m, 0, [], res)
        return res

    def dfs(self, digits, m, level, out, res):
        if level == len(digits) and len(out) > 0:
            res.append("".join(out))
        else:
            s = m[int(digits[level])]
            for ss in s:
                out.append(ss)
                self.dfs(digits, m, level+1, out, res)
                out.pop()
