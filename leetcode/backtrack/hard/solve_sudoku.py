# https://leetcode.com/problems/sudoku-solver/

from collections import defaultdict
from typing import List
from string import digits

def solveSudoku(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)

    digit = set(digits[1:])

    for r in range(9):
        for c in range(9):
            if board[r][c] == '.': continue  # as need to record for filled vals only
            v = board[r][c]

            # record vals of row, col, sqr
            rows[r].add(v)
            cols[c].add(v)
            squares[(r//3,c//3)].add(v)

    def backtrack(r, c):
        if r == 9:
            return True   # all row are traversed
        if c == 9:  
            return backtrack(r+1, 0)  # move to next row

        if board[r][c] != '.':   # already filled
            return backtrack(r, c+1) 
        
        i, j = r//3, c//3  # square coordinates
        # digits which are not present in {row, col, square}
        valid_digits = digit - {*rows[r], *cols[c], *squares[(i,j)]}

        # try placing each digit in curr cell
        for d in valid_digits:
            # 1. record vals of row, col, sqr
            rows[r].add(d)
            cols[c].add(d)
            squares[(i,j)].add(d)
            board[r][c] = d  # place the digit {d} at (r,c) in board

            # 2. Explore next
            res = backtrack(r, c+1)

            if res: return True # {d} at (r,c) is correct choice

            # 3. BackTrack  -> {d} at (r,c) is incorrect; try placing diff digit {d`}
            #    First Undo Prev Choice (before moving to next)
            board[r][c] = '.'
            rows[r].remove(d)
            cols[c].remove(d)
            squares[(i,j)].remove(d)

        return False 

    backtrack(0,0)



board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

ans = solveSudoku(board)

print(ans)