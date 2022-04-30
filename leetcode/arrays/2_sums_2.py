#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List


def twoSum2(nums: List[int], target: int) -> List[int]:
    d = dict()
    for i, n in enumerate(nums):
        diff = target - n 
        if diff <= n and diff in d: # as nums are in non-decreasing order so search in left only
            return [d[diff]+1, i+1]
        d[n] = i

def twoSum2_a2(nums: List[int], target: int) -> List[int]:
    ''' 
        Find right amt of chakura to tradeoff between naruto & sasuke
    '''
    naruto, sasuke = 0, len(nums)-1
    while naruto <= sasuke:
        l, r = nums[naruto], nums[sasuke]
        chakura = l + r
        if chakura == target:
            return [naruto+1, sasuke+1]
        if chakura < target: # need to add more chakura so naruto step forwards
            naruto += 1
        else :  # need to release some chakura so sasuke step backwards
            sasuke -= 1
        




nums = [2,7,11,15] 
target = 9

nums = [2,3,4] 
target = 6

print(twoSum2_a2(nums, target))
    


    
