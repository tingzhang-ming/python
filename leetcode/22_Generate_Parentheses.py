"""
 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.dfs(n, n, "", res)

    def dfs(self, left, right, out, res):
        if left < right:
            return
        if left == 0 and right == 0:
            res.append(out)
            return
        if left > 0:
            self.dfs(left-1, right, out+'(', res)
        if right > 0:
            self.dfs(left, right-1, out+')', res)
