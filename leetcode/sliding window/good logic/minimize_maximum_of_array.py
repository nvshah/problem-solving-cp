# https://leetcode.com/problems/minimize-maximum-of-array/
from math import ceil
from typing import List

def minimizeArrayValue(nums: List[int]) -> int:
    res = total = nums[0]  # As 1st number wont be decreased anymore 

    for i, n in enumerate(nums[1:], 1):
        total += n 
        # 
        # Now in worst case, by settling, max val to individual elem in current sub-list 
        # (ie [0...i]) would be evenly distribution of total (ie average of sub-list)
        avg =  ceil(total / (i+1)) # as we want maximum possible val, so used ceil()

        # As settlement can only happen from right to left, so [avg] is just worst case scenario
        # Settlement can only happen if [n] is > max val of effective previous sub-array
        # if bigger val already exists in previous sub-array then it will be considered as it wont be decrease further any more
        res = max(res, avg)  

    return res