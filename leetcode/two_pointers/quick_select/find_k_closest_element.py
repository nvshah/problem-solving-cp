# https://leetcode.com/problems/find-k-closest-elements/

'''
Techniques : Quick Select (Lamuto)
             Window
             2 Pointers
'''

from typing import List


def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    l, r = 0, len(arr) - 1
    # Lamuto way to Quick Select
    while (r - l + 1) != k:  # till K size window is not found
        dl = abs(arr[l] - x)
        dr = abs(arr[r] - x)

        # Shrink Window (either from left side or right side)
        if dl <= dr:
            r -= 1
        else:
            l += 1

    return arr[l:r + 1]


arr = [1, 2, 3, 4, 5]
k = 4
x = -1

arr = [1, 1, 1, 10, 10, 10]
k = 1
x = 9

arr = [-2, -1, 1, 2, 3, 4, 5]
k = 7
x = 3
ans = findClosestElements(arr, k, x)
print(ans)