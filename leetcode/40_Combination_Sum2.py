"""
 Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:

[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""


class Solution(object):
    def dfs(self, candidates, target, start, out, res):
        if target < 0:
            return
        elif target == 0:
            res.append([o for o in out])
        else:
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                out.append(candidates[i])
                self.dfs(candidates, target - candidates[i], i+1, out, res)
                out.pop()

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.dfs(candidates, target, 0, [], res)
        return res


if __name__ == '__main__':
    s = Solution()
    print s.combinationSum2([1], 1)
