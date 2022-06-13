# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
from typing import List
from itertools import accumulate

'''
Idea : Reverse Greedy Approach
instead of finding minimum elements to remove from end
We will try to find maximum chunk size of subarray which will get remains 
after removal of minimum elements from end 
'''

def minOperations(nums: List[int], x: int) -> int:
    '''Reverse Greedy Approach'''
    dp = [*accumulate(nums, initial=0)]
    lookup = {v:i for i,v in enumerate(dp)}  # reverse mapping for sum -> index
    
    y = sum(nums) - x  # remaining sum after removal of {x}
    cnt = -1  # count for middle chunk subarr size
    for l_val, l_idx in lookup.items():  # l_idx is inclusive
        r_val = l_val + y                 
        if r_val in lookup:
            r_idx = lookup[r_val]  # r_idx is exclusive
            ans = max(r_idx - l_idx, ans)  # try to maximize the middle chunk size
    
    return len(nums) - ans if ans != -1 else -1