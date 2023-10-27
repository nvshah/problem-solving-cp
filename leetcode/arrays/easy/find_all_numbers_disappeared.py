# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
from typing import List 

# O(n) time | O(1) space
def findDisappearedNumbers(nums: List[int]) -> List[int]:
    '''Cyclic Sort'''
    n = len(nums)

    for i in range(n): 
        loc = abs(nums[i])-1
        if nums[loc] > 0 :
            nums[loc] *= -1

    return [i+1 for i in range(n) if nums[i] > 0]

# Test

nums = [4,3,2,7,8,2,3,1]
nums = [1,1]
ans = findDisappearedNumbers(nums) 

print(ans)