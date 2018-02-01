
"""
 Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:

[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution(object):

    def dfs(self, res, level, visited, out, nums):
        if level == len(nums):
            res.append([r for r in out])
            return
        for i in range(len(nums)):
            if not visited[i]:
                if i > 0 and nums[i] == nums[i-1] and visited[i-1] is False:
                    continue
                out.append(nums[i])
                visited[i] = True
                self.dfs(res, level+1, visited, out, nums)
                visited[i] = False
                out.pop()

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        nums.sort()
        visited = [False] * l
        res = []
        self.dfs(res, 0, visited, [], nums)
        return res


if __name__ == '__main__':
    s = Solution()
    print s.permuteUnique([1, 2, 1])
