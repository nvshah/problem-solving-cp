# https://leetcode.com/problems/missing-number/

from typing import List


def missingNumber(nums: List[int]) -> int:
    '''via cyclic sort + linear search'''
    # cyclic sort with modification
    l = len(nums)
    for i in range(l):
        while i != nums[i] != l:
            num = nums[i]
            nums[i], nums[num] = nums[num], num
    
    #print(nums)

    # search first incorrect idx 
    for i in range(l):
        if i != nums[i]:
            return i 
    return l

def missingNumber2(nums: List[int]) -> int:
    '''sum of n natural number'''
    n = len(nums)
    return  (n * (n+1) // 2) - sum(nums)



nums = [3,0,1]
nums = [0,1]
nums = [9,6,4,2,3,5,7,0,1]
nums = [0]

print(missingNumber2(nums))
    

        