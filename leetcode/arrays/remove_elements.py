from typing import List


def removeElement1(nums: List[int], val: int) -> int:
    '''
    Based on Hoare
    '''

    l, r = 0, len(nums)-1
    while l <= r:
        if nums[l] == val:
            nums[l], nums[r] = nums[r], nums[l]  # swap 
            r -= 1  # next slot for {val}
        else:
            l += 1
    return l   # l is pointing to {val}

def removeElement2(nums: List[int], val: int) -> int:
    '''
    Based on Lamuto
    '''
    size = len(nums)
    l = 0  # at the start
    
    for r in range(size):
        if nums[r] != val:  # move it to left part
            nums[l], nums[r] = nums[r], nums[l]
            l += 1  # next slot for left part element
    return l