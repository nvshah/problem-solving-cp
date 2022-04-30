# https://leetcode.com/problems/next-permutation/

from typing import List 
import itertools as it

def rev(arr, l, r):
    while l<r:
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l+1, r-1

def nextPermutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    size = len(nums)

    for i in range(size-1, 0, -1):
        curr, prev = nums[i], nums[i-1]
        if curr > prev:
            # NOTE :- nums[i:] is in decreasing order

            # 1. decide j := find the immediate next elem to `nums[i-1]`
            for j in range(size-1, i-1, -1):
                if nums[j] > prev:
                    break

            # 2. Swap both
            nums[j], nums[i-1] = prev, nums[j]

            # NOTE :- now `nums[j:]` may be not in Decreasing order
            # 3. Recorrect the Disturbed Decreasing Order because of above Swapping
            #    !-> Disturbed Decreasing portion can lie in :- nums[j:]

            for k in range(j, size-1):
                if nums[k] < nums[k+1]:
                    # buuble up 
                    nums[k], nums[k+1] = nums[k+1], nums[k]
                else:
                    # Now the nums[j:] is in Decreasing order
                    break

            # 4. Reverse the Decreasing Part 
            #    NOTE :- this can be done in-place via 2 pointers 
            #nums[i:] = nums[i:][::-1]
            nums[i:] = reversed(it.islice(nums, i, size))

            # 5. Indicator of next permutation available
            break 
    else:
        # Next Perm is not available so reverse the entire array
        nums.reverse()