# https://leetcode.com/problems/sort-colors/

from typing import List
from collections import Counter


def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    BUCKET SORT (as we knew there are 3 distinct element only)
    """
    l = 0
    bucket = Counter(nums)
    for i in [0,1,2]:
        if i in bucket:
            cnt = bucket[i]
            r = l+cnt
            nums[l:r] = [i]*cnt
            l = r

def sortColors2(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    Quick SORT (Lamuto Modified)
    """
    def swap(i, j):
        nums[i], nums[j] = nums[j], nums[i]

    l, r = 0, len(nums)-1
    i = 0
    while i <= r:
        if nums[i] == 0:
            swap(l, i) # swap & move 0 to left side
            l += 1 # next place to put 0
        if nums[i] == 2:
            swap(r, i) # swap & move 2 to right side
            r -= 1 # next place to put 2
            # nullifying {i} ie stay at {i} only
            i -= 1 # as we have not encounter right part so there may be chance of arriving 0 at i
        i += 1

l = [2,0,2,1,1,0]
l = [0,1,2,1,0,2]
#sortColors(l)

# [0,0,1,2,0,2]

sortColors2(l)
print(l)
