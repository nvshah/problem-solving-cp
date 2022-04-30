# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

from typing import List


def arrange_elements(arr):
    '''Arrange maxmimum elements to their correct places'''
    l = len(arr)
    i = 0
    while i < l:
        correct_idx = arr[i] - 1  # correct idx of current element
        if arr[i] != arr[correct_idx]: # duplicate element i.e correct idx already have element placed correctly
            arr[i], arr[correct_idx] = arr[correct_idx], arr[i]  # Swap
        else:
            i+=1

def findDisappearedNumbers(nums: List[int]) -> List[int]:
    ans = []
    arrange_elements(nums) # 1
    print(nums)
    for i in range(len(nums)):
        if nums[i] != i + 1:
            ans.append(i + 1)
    return ans 

# Better Solution (Logic)
def findDisappearedNumbers2(nums: List[int]) -> List[int]:
    '''Inndex Visited UnVisited Logic'''
    for n in nums:
        idx = abs(n)-1
        nums[idx] = -1 * abs(nums[idx])  # -ve, :- num corresp to {idx} exists ie {idx+1}, somewhere in array
    
    return [i+1 for i in range(len(nums)) if nums[i] > 0]  # +ve, :- num corresp to {i} nnot found in array



nums = [4,3,2,7,8,2,3,1]
nums = [1,1]
nums = [4,3,2,7,7,2,3,1]
print(findDisappearedNumbers(nums))

