# Que https://leetcode.com/problems/transpose-matrix/

from typing import List


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    r_l = len(matrix)
    c_l = len(matrix[0])
    return [[matrix[c][r] for c in range(r_l)] for r in range(c_l)]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[1, 2, 3], [4, 5, 6]]
print(transpose(matrix))
