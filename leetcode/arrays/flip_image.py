# https://leetcode.com/problems/flipping-an-image/


from typing import List


def flipAndInvertImage(image: List[List[int]]) -> List[List[int]]:
    return map(lambda i: list(map(lambda n: n ^ 1, reversed(i))), image)


def flipAndInvertImage2(image: List[List[int]]) -> List[List[int]]:
    return [[1 ^ n for n in reversed(r)] for r in image]


l = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
ans = flipAndInvertImage(l)
print(*ans)

# print(*map(operator.inv, reversed([0, 1, 1])))
# print(~1)
