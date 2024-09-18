# https://leetcode.com/problems/convert-1d-array-into-2d-array/description/


from typing import List
from itertools import batched


def construct2DArray(original: List[int], m: int, n: int) -> List[List[int]]:
    if len(original) != m * n:
        return []
    return list(batched(original, n))


def construct2DArray(original: List[int], m: int, n: int) -> List[List[int]]:
    if len(original) != m * n:
        return []
    res = []
    for i in range(m):
        to_skip = n * i
        start, end = to_skip, to_skip + n
        res.append(original[start:end])
    return res


a = [1, 2]
ans = construct2DArray(a, 1, 1)
print(ans)
