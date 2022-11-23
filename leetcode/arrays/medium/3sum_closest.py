# https://leetcode.com/problems/3sum-closest/description/
from typing import List

def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    min_gap = float("inf")
    for i, a in enumerate(nums):
        l, r = i + 1, len(nums) - 1
        while l < r:
            threesum = a + nums[l] + nums[r]
            dif = abs(target- threesum)
            if dif < min_gap:
                min_gap = abs(target - threesum)
                closest = threesum
            if threesum < target:
                l += 1
            elif threesum > target:
                r -= 1
            else:
                return threesum
    return closest