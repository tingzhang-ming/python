"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        l = len(nums)
        nums.sort()
        res = []
        for i in range(l-3):
            for j in range(i+1, l-2):
                left = j + 1
                right = l - 1
                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum == target:
                        out = [nums[i], nums[j], nums[left], nums[right]]
                        if out not in res:
                            res.append(out)
                        left += 1
                        right -= 1
                    elif sum > target:
                        right -= 1
                    else:
                        left += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print s.fourSum([1,0,-1,0,-2,2], 0)
