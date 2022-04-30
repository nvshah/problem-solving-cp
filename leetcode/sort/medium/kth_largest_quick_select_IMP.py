# https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/
from typing import List


def findKthLargest4(nums: List[int], k: int) -> int:
    size = len(nums)
    offset = size - k

    def quick_select(l, r):  # Lamutos way of Selecting
        pivot, ptr = nums[r], l 
        # ptr will point to pos where next smaller elem will be placed
        for i in range(l,r):
            if nums[i] <= pivot:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        nums[ptr], nums[r] = nums[r], nums[ptr]  # place pivot to its correct location

        if offset == ptr: return nums[offset]
        if offset < ptr: return quick_select(l, ptr-1)
        else: return quick_select(ptr+1,r)

    return quick_select(0, size-1)