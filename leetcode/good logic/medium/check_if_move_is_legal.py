#https://leetcode.com/problems/check-if-move-is-legal/
from typing import List

def checkMove(board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
    m = n = 8 # grid size

    directions = [(0,1), (0,-1), (1,0), (-1,0),
                  (1,1), (1,-1), (-1, 1), (-1, -1)]
    
    def isLegal(i, j, clr, direc):
        '''
        i :- row,
        j :- col
        clr :- color of (i,j) cell
        direc :- direction to move from (i,j)
        '''
        x, y = direc  # offset to take forward in corresp direction {direc}
        # current i & j
        ci, cj = i+x, j+y  # skip first cell (i, j) & start from next (as first is assumed to be endpoint)

        length = 1  # track the line of valid length

        while (0 <= ci < m) and (0 <= cj < n):
            if board[ci][cj] == '.': return False # empty cell in between
            length += 1
            if board[ci][cj] == clr: return length >= 3 # length must be >= 3
            ci, cj = ci + x, cj + y 
            
        
        return False 
    
    for d in directions:
        if isLegal(rMove, cMove, color, d): return True 
    
    return False
