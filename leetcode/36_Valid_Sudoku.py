"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated. 
"""


class Solution(object):

    def get_visited(self):
        return {str(i): False for i in range(1, 10)}

    def isValid(self, visited, element):
        if element == '.':
            return True
        if visited[element]:
            return False
        visited[element] = True
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            visited = self.get_visited()
            for j in range(9):
                if not self.isValid(visited, board[i][j]):
                    return False
        for i in range(9):
            visited = self.get_visited()
            for j in range(9):
                if not self.isValid(visited, board[j][i]):
                    return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                visited = self.get_visited()
                for k in range(9):
                    if not self.isValid(visited, board[i+k%3][j+k/3]):
                        return False
        return True

    def isValidSudoku2(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [[] for _ in range(9)]
        col = [[] for _ in range(9)]
        area = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element == '.':
                    continue
                area_id = i/3*3 + j/3
                if element in row[i] or element in col[j] or element in area[area_id]:
                    return False
                else:
                    row[i].append(element)
                    col[j].append(element)
                    area[area_id].append(element)
        return True


if __name__ == '__main__':
    s = Solution()
    b = [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
    print s.isValidSudoku(b)