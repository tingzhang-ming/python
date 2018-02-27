
"""
 Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6. 
"""


class Solution(object):
    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = 0
        l = len(nums)
        all_fu = True
        for i in range(l):
            if nums[i] > 0:
                all_fu = False
                break
        if all_fu:
            return max(nums)
        for i in range(l):
            tmp = 0
            tmp_l = []
            for j in range(i, l):
                tmp += nums[j]
                if tmp <= 0:
                    break
                else:
                    tmp_l.append(nums[j])
                    if tmp > max_value:
                        max_value = tmp
        return max_value
#  Time Limit Exceeded

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        sum = -float("inf")
        res = -float("inf")
        for i in range(l):
            sum = max(nums[i], sum + nums[i])
            res = max(sum, res)
        return res


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    s = Solution()
    print s.maxSubArray(nums)
