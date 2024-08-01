# https://leetcode.com/problems/sort-array-by-parity/

from typing import List


def sortArrayByParity(nums: List[int]) -> List[int]:
    l, r = 0, len(nums)-1
    # l will be next available index for even number
    # r will check if all odd are present on RHS via traversing from end
    while r > l:
        if nums[r] % 2 == 0:  # even number need to be send to Left side
            nums[r], nums[l] = nums[l], nums[r]
            l += 1
        else:  # odd number at its correct side ie RHS
            r -= 1
    return nums

def sortArrayByParity2(nums: List[int]) -> List[int]:
    nums.sort(key= lambda x: x & 1)
    return nums