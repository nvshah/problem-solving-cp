# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from leetcode.BinarySerach.search_in_rotated_sorted_arr import search
from typing import List


def findMin(nums: List[int]) -> int:
    ''' Find min in rotated sorted array 
        # Goal Min values lies in right part
    '''

    l, r = 0, len(nums)-1
    
    if nums[0] < nums[r]: return nums[0]  # Array is not rotated
    
    while l <= r:
        m = (l + r) // 2
        if nums[m] > nums[m+1]:  # boundary between left sorted & right sorted part
            return nums[m+1]
        if nums[l] <= nums[m]:        # {m} lies in Left Sorted Part
            l = m+1    # So boundary for left sorted part is on right side
        else:                         # {m} lies in Right Sorted Part
            #! NOTE : Here including m as anns lies in Right Sorted Part  
            r = m      # So boundary for right sorted part is on left side
    return nums[r]

def findMin2(nums: List[int]) -> int:
    ''' Find min in rotated sorted array 
        # Goal Min values lies in right part
    '''

    l, r = 0, len(nums)-1

    res = nums[0]
    
    # loop till l & r point to right sorted part
    while l <= r:
        if nums[l] < nums[r]:  # l -> r comprise of right sorted part
            return min(res, nums[l])

        m = (l + r) // 2
        # check if elem at {m} is minimum till now or not
        res = min(nums[m], res)

        # {m} lies in Left Sorted Part
        if nums[l] <= nums[m]: 
            # So we need to find the right sorted part      
            l = m+1  
        # {m} lies in Right Sorted Part
        else:
            # Search minimum in right sorted part itself
            r = m-1 
            
nums = [3,4,5,1,2]
nums = [4,5,6,7,0,1,2]
nums = [11,13,15,17]
nums = [6,1,2,3,5]
ans = findMin(nums)

print(ans)