from typing import List

"""
Idea 
transfer to left side from right side 

"""


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        right_sum = sum(nums)  # suffix sum
        left_sum = 0
        ways = 0
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum -= nums[i]
            ways += left_sum >= right_sum
        return ways
