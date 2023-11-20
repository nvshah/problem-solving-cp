# https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/description/
from typing import List 
from collections import Counter

def reductionOperations(nums: List[int]) -> int:
    '''Sort'''
    nums.sort(reverse=True)
    ops = 0 # total operations
    cnt = 0
    for i in range(len(nums)-1):
        cnt += 1
        if nums[i+1] != nums[i]:
            ops += cnt # accumulated count of converted operations
    return ops

def reductionOperations2(nums: List[int]) -> int:
    '''Sort | Map'''
    freqs = Counter(nums)
    elems = sorted(freqs, reverse=True)

    ops = 0 # total operations

    for i in range(len(elems)-1):
        largestFreq = freqs[elems[i]]
        ops += largestFreq # perform operations
        freqs[elems[i+1]] += largestFreq # increase freq of new largest
    
    return ops 



nums = [5, 1, 3] # 3
#nums = [1,1,1] # 0
#nums = [1,1,2,2,3] # 4
ans = reductionOperations(nums)
print(ans)
