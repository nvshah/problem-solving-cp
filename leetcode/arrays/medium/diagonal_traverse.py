# https://leetcode.com/problems/diagonal-traverse
from typing import List

def findDiagonalOrder(mat: List[List[int]]) -> List[int]:
    if not mat: return []

    n, m = len(mat), len(mat[0])
    SIZE = n*m

    def moveDown(r, c):
        '''Move down from [r][c] & return new row, col, direction'''
        direc = -1 # next-direction
        if r == n-1: # last row -> move right
            c += 1
            direc = 1
        elif c == 0: # first col -> move down
            r += 1
            direc = 1
        else:
            r, c = r+1, c-1 # move diagonally down-left
        return r, c, direc
    
    def moveUp(r, c):
        '''Move Up from [r][c] & return new row, col, direction'''
        direc = 1
        if c == m-1: # last col -> move down
            r += 1  
            direc = -1 
        elif r == 0: # first row -> move right
            c += 1
            direc = -1 
        else:
            r, c = r-1, c+1 # move diagonally up-right
        return r, c, direc 
    
    res = [] 
    row, col = 0, 0 # row, col
    direction = 1   # -1 for down & +1 for up
    
    while len(res) != SIZE:
        res.append(mat[row][col])

        if direction == -1:
            row, col, direction = moveDown(row, col)
        else: 
            row, col, direction = moveUp(row, col) 

    return res 

mat = [[1,2,3],[4,5,6],[7,8,9]] # [1, 2, 4, 7, 5, 3, 6, 8, 9]
ans = findDiagonalOrder(mat)
print(ans)