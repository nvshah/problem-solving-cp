
# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

from typing import List
import itertools as it


def findRotation(mat: List[List[int]], target: List[List[int]]) -> bool:
    if mat == target:
        return True
    l = len(mat)
    idx_mat = [(x, y) for x in range(l) for y in range(l)]
    # idx_mat = it.product(range(l), repeat=2)
    # rot 90
    if any((mat[l-1-y][x] != target[x][y] for x, y in idx_mat)):
        # rot 180
        if any((mat[l-1-x][l-1-y] != target[x][y] for x, y in idx_mat)):
            # rot 270
            if any((mat[y][l-1-x] != target[x][y] for x, y in idx_mat)):
                return False
    return True


def findRotation2(mat: List[List[int]], target: List[List[int]]) -> bool:
    if mat == target:
        return True
    for _ in range(3):
        *mat, = zip(*reversed(mat))  # rotate matrix by 90 angle
        # if all((all(sv == tv for sv, tv in zip(s, t)) for s, t in zip(mat, target))):
        if all(tuple(s) == t for s, t in zip(mat, target)):
            return True
    return False

    # mat = ((3-1-y, x) for x, y in it.product(range(3), repeat=2))
    # print(*mat)
mat = [[0, 1], [1, 0]]
target = [[1, 0], [0, 1]]

mat = [[0, 1], [1, 1]]
target = [[1, 0], [0, 1]]

mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
target = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]

ans = findRotation2(mat, target)
print(ans)
