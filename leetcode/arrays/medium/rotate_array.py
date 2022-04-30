# https://leetcode.com/problems/rotate-array/
from typing import List

def rotate1(nums: List[int], k: int) -> None:
    """
     TC := O(n)
     SC := O(1)  // If neglected output arr 
     Non-Inplace Solution
    """
    s = len(nums) # size of {nums}
    e = k % s # effective rotation
    return [nums[i-e] for i in range(s)]

def rotate2(nums: List[int], k: int) -> None:
    """
    Non In-Place 
    TC (O(n))
    """
    e = k % len(nums) # effective rotation
    return nums[-e:] + nums[:-e]

def rotate3(nums: List[int], k: int) -> None:
    """
    3 Reversals (Non-Inplace)
    """
    # Step1 
    nums.reverse()
    # Step2
    return [*reversed(nums[:k]), *reversed(nums[k:])]

def rev(arr, l, r):
    '''reverse the arr inplace from [l,r]'''
    while l<r:
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l+1, r-1
def rotate4(nums: List[int], k: int) -> None:
    """
    IN-PLACE
    3 Reversal Technique
    """
    s = len(nums)
    e = k % s # effective rotation
    if e:
        # Step1 Reverse the List
        #rev(nums, 0, s-1)
        nums.reverse()

        # Step2 Revrse 2 Parts
        rev(nums, 0, k-1)  # 2.1 reverse the first part
        rev(nums, k, s-1)  # 2.2 reverse the second part
    
    



if __name__ == '__main__':
    a = [1,2,3,4,5,6,7]
    k = 3

    nums = [-1,-100,3,99]
    k = 2
    ans = rotate3(nums, k)
    print(ans)