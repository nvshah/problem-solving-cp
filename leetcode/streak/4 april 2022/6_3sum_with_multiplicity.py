# https://leetcode.com/problems/3sum-with-multiplicity/
from collections import defaultdict, Counter
import enum
from math import comb
from typing import List

def threeSumMulti(arr: List[int], target: int) -> int:
    '''
    T.C := O(n^2)
    '''
    freqs = Counter(arr)

    #1. sorted unique nums
    nums = sorted(freqs)
    n = len(nums)
    
    res = 0
    
    print(nums)
    for i, n1 in enumerate(nums): # first elem := {n1}
        t = target - n1 # target for 2 sum
        # Find next 2 elem :- 2 Sum Problem
        l, r = i, n-1  # NOTE :- here {n1} can repeat in soln so consdering l = i
        while l <= r:
            n2, n3 = nums[l], nums[r]
            n23 = n2 + n3
            if n23 < t:
                l += 1
            elif n23 > t:
                r -= 1
            else: # Triplet May be possible for (i, l, r)   
                # the only thing we need to check is Frequency of num available accordingly
                f1, f2, f3 = freqs[n1], freqs[n2], freqs[n3]

                # 1. All 3 are unique num (ie n1, n2, n3)  (So no freq check require)
                if i < l < r:
                    res += f1*f2*f3
                # 2. 2 Uniques (n1, n1, n3) 
                elif (i == l) and (l < r):
                    # f1_C_2 * n3
                    res += (comb(f1, 2) * f3)
                # 3. 2 Unique (n1, n2, n2)
                elif (i < l) and (l == r):
                    # f2_C_2 * f1
                    res += (f1 * comb(f2, 2))
                # 4. All 3 same (ie n1, n1, n1)
                else:
                    res += comb(f1, 3)
                
                # Explore further Possibilities
                l, r = l+1, r-1   # Eg 2, 3, 4, 5  & t = 7 -> (2,5) | (3,4)

    return res % (10**9 + 7)

arr = [1,1,2,2,3,3,4,4,5,5]
target = 8
ans = threeSumMulti(arr, target)
print(ans)