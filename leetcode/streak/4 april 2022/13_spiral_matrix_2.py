# https://leetcode.com/problems/spiral-matrix-ii/
from math import isqrt
from timeit import repeat
from typing import List
import itertools as it

def generateMatrix(n: int) -> List[List[int]]:
    '''
        traverse matrix in spiral order clock-wise  
    '''

    # matrix
    m = [[0]*n for _ in range(n)]

    #! NOTE : r & b are exclusive boundaries
    l, r = 0, n  # left, right
    t, b = 0, n  # top, bottom

    v = 1 # curr val to be filled

    def fill(r, c):
        nonlocal v
        m[r][c], v = v, v+1


    while l<r and t<b:  # till matrxi is not filled/traveresed, spirally

        # 1. fill TOP row (ie from left -> right)
        for j in range(l, r):
            fill(t, j)
        t += 1 # update next top row

        # 2. fill RIGHT col (ie from top -> down)
        for i in range(t, b):
            fill(i, r-1)
        r -= 1 # update right boundary

        if not (l < r and t < b):  # Single row or single col
            break 

        # 3. fill BOTTOM row (ie from right -> left)
        for j in range(r-1, l-1, -1):
            fill(b-1, j)
        b -= 1 # update next bottom row

        # 4. fill LEFT col (ie from bottom -> top)
        for i in range(b-1, t-1, -1):
            fill(i, l)
        l += 1 # update left boundary
    
    return m









