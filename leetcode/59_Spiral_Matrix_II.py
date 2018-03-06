"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,
You should return the following matrix:

[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        num = 1
        matrix = [[0] * n for _ in range(n)]

        tmp = {
            0: [0, 1],
            1: [1, 0],
            2: [0, -1],
            3: [-1, 0]
        }

        m = n
        jilu = [[False] * n for _ in range(m)]
        fangxiang = 0
        x = 0
        y = 0
        end = 0
        tx = ty = 0
        while True:
            if x < m and y < n and jilu[x][y] is False:
                end = 0
                matrix[x][y] = num
                num += 1
                jilu[x][y] = True
                tx = x
                ty = y
            else:
                fangxiang += 1
                if fangxiang > 3:
                    fangxiang = 0
                end += 1
                if end > 1:
                    break
                x = tx
                y = ty
            x += tmp[fangxiang][0]
            y += tmp[fangxiang][1]
        return matrix
