# https://leetcode.com/problems/maximum-erasure-value/
from typing import List

def maximumUniqueSubarray(nums: List[int]) -> int:
    seen = {nums[0]} # elem present in curent window
    total = nums[0]  # total of current window
    l = 0   # left pointer in window
    mx = 0  # ans
    for r in range(1, len(nums)):
        if nums[r] in seen:  # new window
            mx = max(mx, total) 
            # Skip all elem before seen num in curr set
            while True:  
                total -= nums[l]
                seen.remove(nums[l])
                if nums[l] == nums[r]:
                    l += 1
                    break
                l += 1
        seen.add(nums[r])
        total += nums[r]
    
    mx = max(mx, total)
    
    return mx