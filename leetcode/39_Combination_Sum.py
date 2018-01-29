
"""
 Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:

[
  [7],
  [2, 2, 3]
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
                out.append(candidates[i])
                self.dfs(candidates, target-candidates[i], i, out, res)
                out.pop()

    def combinationSum(self, candidates, target):
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
    print s.combinationSum([2, 6, 3, 7], 7)
