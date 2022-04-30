# https://leetcode.com/problems/frequency-of-the-most-frequent-element/

from typing import List 

def maxFrequency(nums: List[int], k: int) -> int:

    l = 0
    res = 0

    # Idea :- Sliding Window of Sorted Array

    # In Sliding Window [l,r] 
    # All element will try to match up the val of last elem of window ie {r}, after k operation
    # & this way we will have mmax frequency := sliding window length

    # Our goal will be to find maximum length sliding window
    # Each element in sliding window will be same after atmost K operations
    
    # 1. Sort 
    nums.sort()

    total = 0  # total val of curr sliding window

    # So after atmost k operation ( total + k <= num[r]*winLen )
    for r in range(len(nums)):
        #winLen = r-l+1  #window length
        last = nums[r]
        total += last  # total val of curr sliding window := sum(nums[l:r+1])
        winLen = r-l+1
        # to get all val samme as {last} element (ie at {r}) in Current Window check :-
        # lastElem * WindowLength <= max val possible of window (including k operation), 
        while (last*winLen) > (total+k):  # till all elements != nums[r]
            # Shrink Window (So that all element in window can become euqal to r via atmost k operations)
            total -= nums[l]  # decrease total by removing first
            l += 1
            winLen -= 1

        # Now window contains all element same = {last}
        res = max(res, winLen)

    return res 

nums = [1,2,4]
k = 5

nums = [1,4,8,13]
k = 5

print(maxFrequency(nums, k))

            



