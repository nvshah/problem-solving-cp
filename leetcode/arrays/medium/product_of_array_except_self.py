# https://leetcode.com/problems/product-of-array-except-self/


from typing import List
from itertools import accumulate


def productExceptSelf(nums: List[int]) -> List[int]:
    size = len(nums)
    ans = [1]*size
    prefix = 1
    for i in range(size):
        ans[i] *= prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(size-1, -1, -1):
        ans[i] *= postfix
        postfix *= nums[i]
    return ans

nums = [1,2,3,4] 
#nums = [-1,1,0,-3,3]  
print(productExceptSelf(nums))
