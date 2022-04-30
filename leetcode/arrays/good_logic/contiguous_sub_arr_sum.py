# https://leetcode.com/problems/continuous-subarray-sum/
from typing import List

def checkSubarraySum(nums: List[int], k: int) -> bool:
    '''
    Idea : Prefix Sum Track the remainders for all Prefix
           &
           Then check if any upcoming prefix also lead to same remainder thus hinting the
           presence of sub-prefix being multiple of {k}
    '''

    # remainder -> index  // ie remainder belong to prefix till {index}
    prefixRemainder = {0:-1}  # 0->-1 is to avoid 2 zeros found at first
    total = 0
    for i, num in enumerate(nums):
        total += num   # prefix_sum := sum(nums[:i+1])
        r = total % k  # remainder
        if r not in prefixRemainder:  # unique remainder for prefix nums[:i+1]
            prefixRemainder[r] = i    # prefix till {i}
        elif i - prefixRemainder[r] >= 2:  # gap between curr index {i} & prev prefix index is more tha 2 thus sub-arr exists
            return True
    return False
