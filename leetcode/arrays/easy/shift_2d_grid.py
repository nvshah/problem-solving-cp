# https://leetcode.com/problems/shift-2d-grid/
from typing import List
import numpy as np

def shiftGrid(grid: List[List[int]], k: int) -> List[List[int]]:
    ''' Via Numpy  '''
    arr = np.array(grid)
    shp = arr.shape    # shape of {arr} ie row, col
    lst = arr.ravel()  # 1-dimen {arr}
    ek = k % len(lst)  # effective k
    nlst = [*lst[-ek:], *lst[:-ek]]  # shift by {ek} := new lst
    narr = np.reshape(nlst, shp) # create new grid from {nlst} of shape {shp}
    return narr

def shiftGrid(grid: List[List[int]], k: int) -> List[List[int]]:
    ''' Via Manual Calc '''
    m, n = len(grid), len(grid[0])

    size = m*n  # total elems in grid

    def coord_to_idx(r, c):
        ''' Convert 2D coordinate to 1D index '''
        return r*n + c 
    
    def idx_to_coord(idx):
        ''' Convert 1D index to coordinate in 2D '''
        return divmod(idx, n)  # n := #cols

    res = [[0]*n for _ in range(m)]

    for r in range(m):
        for c in range(n):
            # find the new loc in {res}
            idx = coord_to_idx(r, c)  # find the corresp idx
            e_idx = (idx + k) % size  # effective idx
            x, y = idx_to_coord(e_idx) # new loc in {res}
            res[x][y] = grid[r][c]

    return res

