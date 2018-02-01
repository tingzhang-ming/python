# encoding: utf-8

"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

沿对角线交换： (i, j) <-> (n-1-j, n-1-i)
沿x轴中线： (i, j) <-> (n-i-1, j)
顺时针旋转：先沿对角线交换， 沿x轴中线   (i, j) <-> (n-1-j, i)

"""


class Solution(object):

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n/2):
            for j in range(i, n-1-i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n - 1 - j][i] = matrix[n-1-i][n-1-j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n-1-i]
                matrix[j][n - 1 - i] = tmp

    def rotate2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n-1):
            for j in range(n-i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][n - 1 - i]
                matrix[n - 1 - j][n - 1 - i] = tmp
        for i in range(n/2):
            for j in range(n):
                matrix[i][j] = matrix[n-1-i][j] ^ matrix[i][j]
                matrix[n-1-i][j] = matrix[n - 1 - i][j] ^ matrix[i][j]
                matrix[i][j] = matrix[n - 1 - i][j] ^ matrix[i][j]


if __name__ == '__main__':
    s = Solution()
    m = [[1,2,3],[4,5,6],[7,8,9]]
    s.rotate(m)
    print m