# https://leetcode.com/problems/maximum-product-of-three-numbers/

from typing import List
import heapq
from sys import maxsize


def maximumProduct1(nums: List[int]) -> int:
    nums.sort()
    
    c1 = nums[0] * nums[1] * nums[-1]    # min1 * min2 * max1
    c2 = nums[-1] * nums[-2] * nums[-3]  # max1 * max2 * max3
    return max(c1, c2)

def maximumProduct2(nums: List[int]) -> int:
    l1 = l2 = l3 = 0
    s1 = s2 = maxsize

    for n in nums:
        if n > l1:
            l1, l2, l3 = n, l1, l2
        elif n > l2:
            l2, l3 = n, l2 
        elif n > l3:
            l3 = n 

        if n < s1:
            s1, s2 = n, s1 
        elif n < s2:
            s2 = n 
    
    print(s1, s2, l1, l2, l3)
    
    return max(s1 * s2 * l1, l1 * l2 * l3)

def maximumProduct3(nums: List[int]) -> int:
    l = heapq.nlargest(3, nums)
    s = heapq.nsmallest(2, nums)

    return max(s[0]*s[1]*l[0], l[0]*l[1]*l[2])

# def maximumProduct4(nums):
#     l = len(nums)
#     i = 0
#     j = l-1
#     t = [0] * 5
#     for _ in range(2):  # pos from rhs -> lhs
#         max_idx = max(range(i, j+1), key=nums.__getitem__) # get max element index/location
#         min_idx = min(range(i, j+1), key=nums.__getitem__)

#         nums[i], nums[min_idx] = nums[min_idx], nums[i]
#         nums[j], nums[max_idx] = nums[max_idx], nums[j]
#         # t[i], t[-i-1] = nums[min_idx], nums[max_idx]

#         i, j = i+1, j-1 
    
#     max_idx = max(range(i, j+1), key=nums.__getitem__)
#     t[-3] = nums[max_idx]

#     return max(t[0]*t[1]*t[-1], t[2]*t[3]*t[4])




# nums = [1,2,3]
# nums = [1,2,3,4]
nums = [-1,-2,-3]

print(maximumProduct3(nums))