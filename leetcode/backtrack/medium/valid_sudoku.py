# https://leetcode.com/problems/valid-sudoku/

from typing import List
from collections import defaultdict


def isValidSudoku(board: List[List[str]]) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)

    # Imagine 1 Matrix where each square is a cell ie 3 * 3 matrix
    # Formula to get cell coordinate of Square in 3*3 matrix

    for r in range(9):
        for c in range(9):
            if board[r][c] == '.': continue  # as need to check for filled val only

            # determine the square 
            #   -> Each Square is single cell in 3*3 Matrix
            i, j = r//3, c//3
            v = board[r][c]

            # dup_in_row = v in rows[r]  # is duplicate of {v} present in row {r}
            # dup_in_col = v in cols[c]  # is duplicate of {v} present in col {c}
            # dup_in_sqr = v in squares[(i,j)] # is duplicate of {v} present in square(i,j)

            # is duplicate of {v} present in row, col, or Square
            if (v in rows[r]) or (v in cols[c]) or (v in squares[(i,j)]):
                return False 
            
            # record vals of row, col, sqr
            rows[r].add(v)
            cols[c].add(v)
            squares[(i,j)].add(v)

    return True

def isValidSudoku2(board: List[List[str]]) -> bool:
    vals = set()
    for r in range(9):
        for c in range(9):
            v = board[r][c]
            print(board[r][c])
            i, j = r//3, c//3
            if v != '.': 
                rv = v+f'r{r}'
                if rv in vals: return False 
                vals.add(rv)
                cv = v+f'c{c}'
                if cv in vals: return False 
                vals.add(cv)
                sqv = v+f'sq{i}{j}'
                if sqv in vals: return False 
                vals.add(sqv)
    return True

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


print(isValidSudoku2(board))