# encoding: utf-8
"""
Implement next permutation,
which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible,
it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples.
Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

1　　2　　7　　4　　3　　1

1　　2　　7　　4　　3　　1

1　　3　　7　　4　　2　　1

1　　3　　1　　2　　4　　7
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        j = n - 1
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            while nums[j] <= nums[i]:
                j -= 1
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        tmp = nums[i+1:]
        tmp.reverse()
        for k in range(i+1, n):
            nums[k] = tmp[k-i-1]

