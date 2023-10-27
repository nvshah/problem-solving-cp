# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/

from typing import List


def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
    # Intiial Values
    curSum = sum(arr[:k])
    res = int((curSum/k) >= threshold)

    # Window defined by [l:r]
    l, r = 0, k-1
    for r in range(k, len(arr)):
        # remove from left & add from right
        curSum += arr[r] - arr[l]

        if (curSum/k) >= threshold:
            res += 1
        l += 1
    return res 

# TEST

arr = [2,2,2,2,5,5,5,8]
a = numOfSubarrays(arr, 3, 3)
print(a)  # 4