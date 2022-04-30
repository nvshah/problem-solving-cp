# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List
from math import ceil

'''
(As given that first element of each row is > than prev row element)

So perform binary search 2 time ( modified + standard )

Steps :-

pick 1st column
find the candidate row for target element via modified Binary Search on that first column
Apply normal binary Search on founded canidate row
Complexity :- O(log(nm))
'''


def binary_search(arr, t):
    s, e = 0, len(arr)-1
    while s <= e:
        m = s + (e - s) // 2
        if arr[m] == t:
            return m
        elif t > arr[m]:
            s = m+1
        else:
            e = m-1
    return -1

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    r_s, r_e = 0, len(matrix)-1
    while r_s != r_e: 
        m = ceil((r_s + r_e) / 2) # giving priority to rhs idx
        num = matrix[m][0]
        if num == target:
            return True
        elif target > num:
            r_s = m  # target can be in middle row so r_s -> m
        else:
            r_e = m-1  # target will always beyond middle row at moment
    idx = binary_search(matrix[r_s], target)
    return idx != -1



matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 10

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13

matrix = [[-9, -8, -8], [-5, -3, -2], [0, 2, 2], [4, 6, 8]]
target = 15

matrix = [[-8, -7, -5, -3, -3, -1, 1], 
         [2, 2, 2, 3, 3, 5, 7], 
         [8, 9, 11, 11, 13, 15, 17],
          [18, 18, 18, 20, 20, 20, 21], 
          [23, 24, 26, 26, 26, 27, 27], 
          [28, 29, 29, 30, 32, 32, 34]]
target = -5


print(searchMatrix(matrix, target))
