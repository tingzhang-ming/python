
"""
 Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution(object):

    def dfs(self, res, level, visited, out, nums):
        if level == len(nums):
            res.append([r for r in out])
            return
        for i in range(len(nums)):
            if not visited[i]:
                out.append(nums[i])
                visited[i] = True
                self.dfs(res, level+1, visited, out, nums)
                visited[i] = False
                out.pop()

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        visited = [False] * l
        res = []
        self.dfs(res, 0, visited, [], nums)
        return res


if __name__ == '__main__':
    s = Solution()
    print s.permute([1, 2, 3])
