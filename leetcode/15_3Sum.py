
"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        count = {}
        for i in set(nums):
            count[i] = nums.count(i)
        pos = [i for i in count if i > 0]
        nag = [i for i in count if i < 0]
        res = []
        if 0 in count and count[0] > 2:
            res.append([0, 0, 0])
        for i in pos:
            for j in nag:
                r = - i -j
                if r in count:
                    if (r == i or r == j) and count[r] > 1:
                        res.append([j, r, i])
                    if r == 0:
                        res.append([j, r, i])
                    if r > i:
                        res.append([j, i, r])
                    if r < j:
                        res.append([r, j, i])
        return res
