"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        nums.sort()
        cha = float("inf")
        res = 0
        end = False
        for i in range(l-2):
            left = i+1
            right = l-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if abs(sum - target) < cha:
                    cha = abs(sum - target)
                    res = sum
                if sum > target:
                    right -= 1
                elif sum == target:
                    end = True
                    res = sum
                    break
                else:
                    left += 1
            if end:
                break
        return res

