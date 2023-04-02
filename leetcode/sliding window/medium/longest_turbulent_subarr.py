# https://leetcode.com/problems/longest-turbulent-subarray/
from typing import List

'''
IDEA
---
Sliding Window (2 pointer)
- keeping track of previous sign-equality
'''

def maxTurbulenceSize(arr: List[int]) -> int:
    l, r = 0, 1 
    prev = '' # for beginning there wont be any sign
    ans = 1  # by default single element would be there atleast in a turbulence sub-arr
    size = len(arr)

    while r < size:
        if arr[r-1] < arr[r] and prev != '<':
            # current turb proceeds
            #cur_turb_size += 1
            prev = '<'
            r += 1
        elif arr[r-1] > arr[r] and prev != '>':
            # current turb proceeds
            #cur_turb_size += 1
            prev = '>'
            r += 1
        else:
            # track optimal turb size
            cur_turb_size = r-l
            ans = max(ans, cur_turb_size)

            # new turb to be discovered
            if arr[r-1] == arr[r]:
                # need to step ahead as '==' is not considered in turbulence
                r += 1
            l = r-1 # {l} always lie 1 step behind {r} in new discovery of turbulence !
            # reset turb-info
            prev = ''
            
    ans = max(ans, r-l)  # check for one last time as r exhausted
    return ans

def maxTurbulenceSize2(arr: List[int]) -> int:
    l = r = 0
    prev = '' # for beginning there wont be any sign
    ans = 1  # by default single element would be there atleast in a turbulence sub-arr
    size = len(arr)

    while r < size-1:
        if arr[r] < arr[r+1] and prev != '<':
            # current turb proceeds
            prev = '<'
            r += 1
        elif arr[r] > arr[r+1] and prev != '>':
            # current turb proceeds
            prev = '>'
            r += 1
        else:
            # track optimal turb size
            cur_turb_size = r-l+1
            ans = max(ans, cur_turb_size)

            # new turb to be discovered
            if arr[r] == arr[r+1]:
                # need to step ahead as '==' is not considered in turbulence
                r += 1
            l, prev = r, '' # reset turb-info (new discovery of turbulence)
            
    return max(ans, r-l+1)  # check for one last time as r exhausted