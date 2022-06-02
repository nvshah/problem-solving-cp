# https://leetcode.com/problems/transpose-matrix/
from typing import List

def transpose(matrix: List[List[int]]) -> List[List[int]]:
    #return [[matrix[c][r] for c in range(len(matrix))] for r in range(len(matrix[0]))]
    return zip(*matrix)