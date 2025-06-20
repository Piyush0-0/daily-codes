#36. Valid Sudoku
# Determine if a 9 x 9 Sudoku board is valid. Only the filled 
# cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the 
# digits 1-9 without repetition.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in board:
            y=[]
            for i in x:
                if (i not in y) or (i=='.'):
                    y.append(i)
            if y!=x:
                return False
        for x in range(9):
            for y in range(9):
                a=board[y][x]
                if a!=".":
                    for z in range(y+1,9):
                        b=board[z][x]
                        if a==b:
                            return False
        for x in range(0,9,3):
            for y in range(0,9,3):
                for m in range(x,x+3):
                    for n in range(y,y+3):
                        a=board[m][n]
                        if a!=".":
                            for i in range(x,x+3):
                                for j in range(y,y+3):
                                    if m!=i and n!=j:
                                        b=board[i][j]
                                        if a==b:
                                            return False

        return True