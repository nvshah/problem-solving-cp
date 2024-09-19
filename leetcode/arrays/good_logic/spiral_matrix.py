# https://leetcode.com/problems/spiral-matrix/

from typing import List


"""
Logic :
Repeat till matrix is consumed
{
step 1) Extract First Row & append all elements to ans list
step 2) Reverse Each Row
step 3) Transpose of resulted matrix
}

Logic2: (similar but more concise)
Repeat till matrix exists
{
S 1) Get First Row
S 2) Rotate Matrix by 90 deg left side (ie Antic-Clockwise)
     2.1 Rotate (Transpose)
     2.2 Reverse 
}

"""


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    """
    traverse matrix in spiral order clock-wise
    """
    spiral_traverse = []

    def rotate_left(m):
        """
        In-Place
        [1, 2]
        [3, 4]

        [2, 4]
        [1, 3]
        """
        (*m,) = zip(m)  # transpose
        m.reverse()  # = 90 degree (left) rotation

    while matrix:
        first_row = matrix.pop(0)
        spiral_traverse.extend(first_row)
        rotate_left(matrix)

    return spiral_traverse


def spiralOrder2(matrix: List[List[int]]) -> List[int]:
    """
    traverse matrix in spiral order clock-wise
    """
    spiral_traverse = []
    while matrix:
        first_row = matrix.pop(0)
        spiral_traverse.extend(first_row)
        matrix = list(zip(*map(reversed, matrix)))
    return spiral_traverse


def reverseSpiralOrder(matrix: List[List[int]]) -> List[int]:
    """
    traverse matrix in spiral order anti-clock-wise
    Steps :- 1) Transpose of a given matrix
             2) Do a Spiral Order Traverse
    """
    (*matrix,) = zip(*matrix)
    anti_spiral_traverse = spiralOrder2(matrix)
    return anti_spiral_traverse


def spiralOrder3(matrix: List[List[int]]) -> List[int]:
    m, n = len(matrix), len(matrix[0])  # Initial possible number of steps
    direction = 1  # Start off going right
    i, j = 0, -1
    output = []
    while m * n > 0:
        for _ in range(n):  # move horizontally
            j += direction
            output.append(matrix[i][j])
        m -= 1
        for _ in range(m):  # move vertically
            i += direction
            output.append(matrix[i][j])
        n -= 1
        direction *= -1  # flip direction
    return output


def spiralOrder4(matrix: List[List[int]]) -> List[int]:
    """4 pointers approach"""
    m, n = len(matrix), len(matrix[0])
    res = []

    #! NOTE : r & b are exclusive boundaries
    l, r = 0, n  # left, right
    t, b = 0, m  # top, bottom

    while l < r and t < b:  # till matrix is not filled/traveresed, spirally

        # 1. fill TOP row (ie from left -> right)
        for j in range(l, r):
            res.append(matrix[t][j])
        t += 1  # update next top row

        # 2. fill RIGHT col (ie from top -> down)
        for i in range(t, b):
            res.append(matrix[i][r - 1])
        r -= 1  # update right boundary

        if not (l < r and t < b):  # Single row or single col
            break

        # 3. fill BOTTOM row (ie from right -> left)
        for j in range(r - 1, l - 1, -1):
            res.append(matrix[b - 1][j])
        b -= 1  # update next bottom row

        # 4. fill LEFT col (ie from bottom -> top)
        for i in range(b - 1, t - 1, -1):
            res.append(matrix[i][l])
        l += 1  # update left boundary

    return res


def test_reverse():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    matrix = [[1, 10], [2, 11], [3, 12]]
    #   ans1 = spiralOrder(matrix)
    ans2 = reverseSpiralOrder(matrix)

    # print(ans1)
    print(ans2)


def test():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ans = spiralOrder(matrix)
    print(ans)


test()
