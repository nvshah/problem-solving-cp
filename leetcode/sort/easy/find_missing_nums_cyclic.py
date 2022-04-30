# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

from ast import List


def findDisappearedNumbers1(nums: List[int]) -> List[int]:
    '''Via Cyclic Sort''' 
    i, l = 0, len(nums)
    while i < l:
        correct_idx = nums[i] - 1  # correct idx of current element
        if nums[correct_idx] != nums[i]:
            # move element to its correct index
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]  # Swap
        else:
            i += 1
    
    return [i+1 for i in range(l) if nums[i]-1 != i]

