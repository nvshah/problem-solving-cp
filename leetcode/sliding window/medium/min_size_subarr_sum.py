# https://leetcode.com/problems/minimum-size-subarray-sum/description/
from typing import List 

def minSubArrayLen(target: int, nums: List[int]) -> int:
    ''' BETTER '''
    l, r = 0, 0
    minLen = len(nums)+1
    curSum = 0
    for r in range(len(nums)): # Expand window via 1 step
        if nums[r] >= target:  # Single number (Edge Case)
            return 1
        
        curSum += nums[r]

        # ! In worst case entire window gets shrinked (ie curSum = 0, l -> r+1) & this will stop while loop as target > 1
        while curSum >= target:  
            # note the window size
            minLen = min(minLen, r-l+1) 

            # try to reduce window
            curSum -= nums[l]  # remove [l] from current total
            l += 1  # remove [l] via shrinking window

    return minLen % (len(nums)+1)

def minSubArrayLen1(target: int, nums: List[int]) -> int:
    l, r = 0, 0
    minLen = len(nums)+1
    curSum = 0
    for r in range(len(nums)):
        curSum += nums[r]

        if curSum >= target:
            # try to reduce window
            while l <= r:
                curSum -= nums[l] # check removing [l]
                if curSum < target: # removing failed
                    curSum += nums[l] # so revert (undo) last operation
                    break
                l += 1 # remove [l]
            
            # update min len 
            minLen = min(minLen, r-l+1)

    return minLen % (len(nums)+1)

target = 7 
nums = [2,3,1,2,4,3]

a = minSubArrayLen(target, nums)
        
print(a)
        
        




