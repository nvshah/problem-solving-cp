# number_of_zero_filled_sub_arr.py
# https://leetcode.com/problems/number-of-zero-filled-subarrays/
from typing import List 
from itertools import takewhile, dropwhile
from operator import not_
import cardinality

'''
#cnts    -> possible-combinations
i        -> c
--------------
1 (0)    -> 1    // 0 + 1
2 (00)   -> 3    // 1 + 2 
3 (000)  -> 6    // 3 + 3
4 (0000) -> 10   // 6 + 4

_________________________

i        -> (c-1 + i)

In other words when the cnt is {i} := ans is (1 + 2 + ... + i) => (i * (i+1) / 2)
'''

def zeroFilledSubarray(nums: List[int]) -> int:
    '''Time limit issue'''
    ans, i, total = 0, 0, len(nums)
    while i < total:
        cnt = 0
        while (i < total) and (nums[i] == 0):
            cnt, i = cnt+1, i+1
            ans += cnt 
        i += 1
    return ans


def zeroFilledSubarray_o1(nums: List[int]) -> int:
    '''Time limit issue'''
    trav = iter(nums)
    ans = 0
    while trav:
        trav = dropwhile(bool, trav) # drop non-zeros
        t = takewhile(not_, trav)
        cnt = cardinality.count(t)
        if cnt:
            ans += cnt * (cnt + 1) // 2 
        else:
            break
    return ans

nums = [1,3,0,0,2,0,0,4]
#nums = [0,0,0,2,0,0]
print(zeroFilledSubarray(nums))