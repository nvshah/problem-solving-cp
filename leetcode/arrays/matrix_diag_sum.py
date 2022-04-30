# https://leetcode.com/problems/matrix-diagonal-sum/

from typing import List

# Complexity -> O(n/2)


def diagonalSum(mat: List[List[int]]) -> int:
    sum = 0
    l = len(mat)
    m = l // 2
    for i in range(m):
        sum += mat[i][i] + mat[i][-1-i] + mat[-1-i][i] + mat[-i-1][-1-i]
    if l & 1 or not m:
        # Odd or 1*1 matrix
        sum += mat[m][m]

    return sum


mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

mat = [[1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1]]

mat = [[5]]

mat = [[6, 3, 1, 10, 7, 4],
       [4, 10, 1, 9, 5, 10],
       [5, 5, 7, 3, 8, 5],
       [2, 7, 6, 4, 7, 6],
       [7, 9, 6, 1, 8, 5],
       [1, 7, 9, 5, 8, 4]]

print(diagonalSum(mat))
