# https://leetcode.com/problems/move-zeroes/

from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    size = len(nums)
    l, r = 0, size-1

    def swap(i, j):
        nums[i], nums[j] = nums[j], nums[i]

    while l < r:
        if nums[l] == 0:
            swap(l, r)
            r -= 1
        else:
            l += 1

def moveZeroes2(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    size = len(nums)
    l = r = 0

    def swap(i, j):
        nums[i], nums[j] = nums[j], nums[i]

    #while r < size:
    for r in range(size):
        print(l)
        if nums[l] != 0:
            l += 1
        else:
            if nums[r] != 0:
                swap(l, r)
                l += 1
        #r += 1 

def moveZeroes3(nums: List[int]) -> None:
    l = 0  # pointer 1
    # {l} will keep hold of position for non-zero element to be placed
    
    for r in range(len(nums)):  # r is second pointer
        if nums[r] != 0:   # found non-zero number so inform {l} about it
            nums[l], nums[r] = nums[r], nums[l]  # swap 
            l += 1  # l now point to next avail pos for non-zero element
            

nums = [0,1,0,3,12]
#nums = [1, 2, 0, 4, 0, 0, 13, 20, 0]
moveZeroes2(nums)
print(nums)



