# 54. Spiral Matrix
# Given an m x n matrix, return all elements of the matrix
# in spiral order.


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        a=[]
        m=len(matrix)
        n=len(matrix[0])
        c1,c2,r1,r2=0,n-1,0,m-1
        x,y=0,0
        while len(a)<(m*n):
            while y<=c2:
                if len(a)<(m*n):
                    a.append(matrix[x][y])
                y+=1
            y-=1
            x+=1
            r1+=1
            while x<=r2:
                if len(a)<(m*n):
                    a.append(matrix[x][y])
                x+=1
            x-=1
            y-=1
            c2-=1
            while y>=c1:
                if len(a)<(m*n):
                    a.append(matrix[x][y])
                y-=1
            y+=1
            x-=1
            r2-=1
            while x>=r1:
                if len(a)<(m*n):
                    a.append(matrix[x][y])
                x-=1
            x+=1
            y+=1
            c1+=1
        return a
