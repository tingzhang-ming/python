# encoding: utf-8
"""
在二维坐标系中，(i, ai) 表示 从 (i, 0) 到 (i, ai) 的一条线段，
任意两条这样的线段和 x 轴组成一个木桶，找出能够盛水最多的木桶，返回其容积。

用两个指针从两端开始向中间靠拢，如果左端线段短于右端，那么左端右移，反之右端左移，直到左右两端移到中间重合，
记录这个过程中每一次组成木桶的容积，返回其中最大的

合理性解释：当左端线段L小于右端线段R时，我们把L右移，这时舍弃的是L与右端其他线段（R-1, R-2, ...）组成的木桶，
这些木桶是没必要判断的，因为这些木桶的容积肯定都没有L和R组成的木桶容积大
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        res = 0
        if l < 2:
            return res
        a = 0
        b = l - 1
        while a <= b:
            tmp = (b - a) * min(height[a], height[b])
            if tmp > res:
                res = tmp
            if height[a] < height[b]:
                a += 1
            else:
                b -= 1
        return res
