"""
Given an array of integers sorted in ascending order,
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx = self.search(nums, 0, len(nums)-1, target)
        if idx == -1:
            return [-1, -1]
        left = right = idx
        while left > 0 and nums[left-1] == nums[idx]:
            left -= 1
        while right < len(nums) - 1 and nums[right+1] == nums[idx]:
            right += 1
        return [left, right]

    def search(self, nums, left, right, target):
        if left > right:
            return -1
        mid = (left + right) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.search(nums, mid + 1, right, target)
        else:
            return self.search(nums, left, mid - 1, target)
