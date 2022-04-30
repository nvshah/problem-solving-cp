# https://leetcode.com/problems/intersection-of-two-arrays-ii/

from typing import List

from collections import Counter as ctr

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    if len(nums1) > len(nums2):
        s_l, b_l = nums2, nums1 
    else:
        s_l, b_l = nums1, nums2 
    freq_s_l = ctr(s_l)
    ans = []
    for n in b_l:
        cnt = freq_s_l.get(n, 0)
        if cnt:
            ans.append(n)
            freq_s_l[n] -= 1
    return ans


a1 = [1,2,2,2,2,2,1]
a2 = [2,22,2,2,2]

anns = intersect(a1, a2)
print(anns)
