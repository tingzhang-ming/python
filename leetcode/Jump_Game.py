"""
 Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false. 
"""


class Solution(object):

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        cover = 0
        for i in range(l):
            if cover >= l-1:
                return True
            if cover >= i:
                cover = max(cover, i + nums[i])
        return False

    def canJump2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        l = len(nums)
        if l == 1:
            return True
        b = [False] * l
        que = list()
        que.append(0)
        tmp = 0
        while len(que) > 0:
            index = que.pop()
            if b[index]:
                continue
            max_jump = index + nums[index]
            b[index] = True
            if max_jump >= l-1:
                return True
            if max_jump > tmp:
                que.extend(range(tmp+1, max_jump+1))
                tmp = max_jump
        return False


if __name__ == '__main__':
    print Solution().canJump([2, 0, 0])

