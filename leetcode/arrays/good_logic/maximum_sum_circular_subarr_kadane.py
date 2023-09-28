# https://leetcode.com/problems/maximum-sum-circular-subarray/submissions/
from typing import List


'''
Idea: 
Candidate 1:
First try finding max sub array -> (without considering circular)

Candidate 2:
Now If we consider circular sub-array then find min-sub-array and rest all will be max sub array
possible 
So this min-subarr will be dividing main arr in 2 halfs & these 2 halfs are individually > this min-subarr
and both are connected in circcular manner (for sure)
So this can be candidate 2

So using Kadane algo we will find both max-sub-arr & min-sub-arr
'''

def maxSubarraySumCircular(nums: List[int]) -> int:
    '''Kadane's Algo | Greedy'''
    cMin = cMax = gMax = gMin = nums[0]

    for n in nums[1:]:
        cMax = max(cMax + n, n)
        gMax = max(gMax, cMax)

        cMin = min(cMin + n, n)
        gMin = min(gMin, cMin)
    
    if gMax < 0:
        # all the elements in nums are -ve, hence there is no purpose of looking for circular combinations
        return gMax 
    cand1 = gMax 
    cand2 = sum(nums) - gMin  # combine left + right of min-subarr (ie due to circular possibility) 

    return max(cand1, cand2)

    

