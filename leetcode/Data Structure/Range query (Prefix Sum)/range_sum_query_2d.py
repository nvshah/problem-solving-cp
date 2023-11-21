# https://leetcode.com/problems/range-sum-query-2d-immutable/

import pprint
from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        # add dummy row & column at top & left for easy calc
        dummy_row = [0]*(n+1) 
        dummy_cols = [[0, *r] for r in matrix]
        self.matrix = [dummy_row, *dummy_cols] # with dummy col
        
        # compute sum-region for each cell from top-left corner
        # assuming current cell as bottom right corner
        for i in range(1, m+1):
            prefixSum = 0
            for j in range(1, n+1):
                prefixSum += self.matrix[i][j]
                aboveSum = self.matrix[i-1][j]
                self.matrix[i][j] = prefixSum + aboveSum

        pprint.pprint(self.matrix)
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1+1, col1+1, row2+1, col2+1  # as we added dummy row & col earlier
        bottom_right = self.matrix[r2][c2] # entire
        above = self.matrix[r1-1][c2]
        left = self.matrix[r2][c1-1]
        top_left = self.matrix[r1-1][c1-1]  # this gonna removed twice so need to add manually in final ans
        return bottom_right - above - left + top_left

m1 = [     
    [2, 1, 4, 3], 
    [1, 1, 2, 2],
    [1, 2, 2, 4],
]
m2 = [
            [3, 0, 1, 4, 2], 
            [5, 6, 3, 2, 1], 
            [1, 2, 0, 1, 5], 
            [4, 1, 0, 1, 7], 
            [1, 0, 3, 0, 5]
        ] 
n = NumMatrix(m2)
print(n.sumRegion(*m1[0]))



