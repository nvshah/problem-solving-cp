# https://leetcode.com/problems/game-of-life/
from typing import List

def gameOfLife(board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.

    """
    # Mappings
    # Original | New | State 
    #    0     |  0  |  0
    #    1     |  0  |  1
    #    0     |  1  |  2
    #    1     |  1  |  3


    # ROWS, COLS
    m, n = len(board), len(board[0])

    def cntNeighbors(r, c):
        cnt = 0
        for i in range(r-1, r+2):
            for j in range(c-1, c+2):
                if (i==r and j==c) or i<0 or j<0 or i==m or j==n:
                    continue # edge cases (boundaries)
                if board[i][j] in [1,3]:
                    cnt += 1 
                
        return cnt 
    
    for r in range(m):
        for c in range(n):
            nei = cntNeighbors(r, c)
            if board[r][c] == 1: # alive
                if nei in [2,3]:  
                    board[r][c] = 3  # lives on to the next gen.
            elif nei == 3:  # dead but 3 alive neighbors
                board[r][c] = 2  # so gets alive in next gen
    
    for r in range(m):
        for c in range(n):
            board[r][c] = 1 if board[r][c] > 1 else 0 # as per Mappings
