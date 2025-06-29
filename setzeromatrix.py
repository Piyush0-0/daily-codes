# 73. Set Matrix Zeroes
# Given an m x n integer matrix matrix, if an element is 0, set its 
# entire row and column to 0's.
# You must do it in place.


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        def lol(a,b):
            for x in range(j):
                if matrix[a][x]!=0:
                    matrix[a][x]=-69
            for x in range(i):
                if matrix[x][b]!=0:
                    matrix[x][b]=-69
        i=len(matrix)
        j=len(matrix[0])
        for x in range(i):
            for y in range(j):
                if matrix[x][y]==0:
                    lol(x,y)
        for x in range(i):
            for y in range(j):
                if matrix[x][y]==-69:
                    matrix[x][y]=0
        return matrix

        