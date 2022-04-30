# https://leetcode.com/problems/rotate-image/


from typing import List


def doTransposeOf(mat):
    '''
    Inplace Transpose i.e m[i][j] = m[j][i]
    '''
    r = len(mat)
    for i in range(r-1):
        for j in range(i+1, r):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]  # Swap


def reverseBy2Pointer(l):
    for i in range(len(l)//2):
        l[i], l[-i-1] = l[-i-1], l[i]  # Swap


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """

    # Step 1 -> transpose of a Matrix
    doTransposeOf(matrix)

    # Step 2 -> reverse each row
    for r in matrix:
        r.reverse()

    return matrix


def rotate2(matrix: List[List[int]]) -> None:
    '''90 deg clockwise rotation but not inplace'''
    matrix.reverse()
    return zip(*matrix)



matrix = [[1,2,3],[4,5,6],[7,8,9]]

# ans = rotate(matrix=matrix)

# print(ans)

ans = rotate2(matrix)

print(*ans)

