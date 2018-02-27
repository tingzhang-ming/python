"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

You should return [1,2,3,6,9,8,7,4,5]. 
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        tmp = {
            0: [0, 1],
            1: [1, 0],
            2: [0, -1],
            3: [-1, 0]
        }
        m = len(matrix)
        n = len(matrix[0])
        jilu = [[False] * n for _ in range(m)]
        res = []
        fangxiang = 0
        x = 0
        y = 0
        end = 0
        tx = ty = 0
        while True:
            if x < m and y < n and jilu[x][y] is False:
                end = 0
                res.append(matrix[x][y])
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
        return res


if __name__ == '__main__':
    m = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
    s = Solution()
    print s.spiralOrder(m)

