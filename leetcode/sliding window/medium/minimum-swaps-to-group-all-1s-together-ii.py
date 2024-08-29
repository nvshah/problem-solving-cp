# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

from typing import List

'''
Idea : 

Find window having max-ones

For circular array detection we will simulate the array being appended by itself
'''


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums) 
        ideal_window_size = nums.count(1) # total_ones

        # sliding window pointers
        l = 0
        r = ideal_window_size

        cur_window_ones_count = nums[l: r].count(1) # initialize with first window 
        max_possible_ones_count = cur_window_ones_count

        for i in range(r, 2*N): # 2* N = to simulate extended array (by merging same array at end to itself)
            left = l % N 
            right = i % N 

            popped = nums[left] 
            l += 1
            if popped == 1: 
                cur_window_ones_count -= 1

            if nums[right] == 1:
                cur_window_ones_count += 1 
            
            max_possible_ones_count = max(max_possible_ones_count, cur_window_ones_count)
        
        return ideal_window_size - max_possible_ones_count #  = operations to swap 





