# https://leetcode.com/problems/merge-sorted-array/

from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # IDEA :- start placing correct element from end
		
    m, n, k = m-1, n-1, m+n-1  # k is last_idx of nums1

    while m >= 0 and n >= 0:  # till either nums1 or nums2 get exhausted
        if nums1[m] > nums2[n]:
            nums1[k] = nums1[m]
            m -= 1
        else:
            nums1[k] = nums2[n]
            n -= 1
        k -= 1
        
    # if nums2 get exhausted then its fine as nums1 is already sorted in its place
    # but if nums1 get exhausted then we need to place element from nums2 into nums1 correctly
    
    while n >= 0:  # if any num left to be discovered in nums2
        nums1[k], k, n = nums2[n], n-1, k-1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)