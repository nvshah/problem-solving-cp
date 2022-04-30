# https://leetcode.com/problems/lucky-numbers-in-a-matrix/


from typing import List
from operator import itemgetter


def transpose_of_matrix(mat):
    return zip(*mat)


def luckyNumbers(matrix: List[List[int]]) -> List[int]:
    col_max = [max(c) for c in zip(*mat)]
    ans = []
    for r in matrix:
        i, e = min(enumerate(r), key=itemgetter(1))
        if col_max[i] == e:
            ans.append(e)
    return ans


mat = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
#t_mat = [(3, 9, 15), (7, 11, 16), (8, 13, 17)]

#transpose_mat = transpose_of_matrix(mat)

mat = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]

mat = [[7, 8], [1, 2]]

mat = [[3, 6], [7, 1], [5, 2], [4, 8]]

ans = luckyNumbers(mat)

print(ans)
