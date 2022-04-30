# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

from typing import List

# O(m + n + k)  where k is the len(indices)


def oddCells(m: int, n: int, indices: List[List[int]]) -> int:
    rows = [0]*m
    cols = [0]*n
    for r, c in indices:
        rows[r] = 1 ^ rows[r]
        cols[c] = 1 ^ cols[c]

    odd_r = sum(rows)
    odd_c = sum(cols)
    ((odd_r) * (n - odd_c)) + ((odd_c) * (m - odd_r))
