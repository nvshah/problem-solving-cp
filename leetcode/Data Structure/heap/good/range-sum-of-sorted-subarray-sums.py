# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

from typing import List
import heapq


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        subarr_sums = []

        for i in range(n):
            cur_sum = 0
            for j in range(i, n):
                cur_sum += (cur_sum + nums[j]) % MOD
                subarr_sums.append(cur_sum)

        subarr_sums.sort()

        return sum(subarr_sums[left - 1 : right]) % MOD

    def rangeSumA2(self, nums: List[int], n: int, left: int, right: int) -> int:
        """Via Heap"""
        MOD = 10**9 + 7
        # Heap -> (subbarr_sum, next-position)
        min_heap = [(num, i+1) for i, num in enumerate(nums)]
        heapq.heapify(min_heap)

        def activity():
            total, r_idx = heapq.heappop(min_heap)
            if r_idx < n:
                next_num = nums[r_idx]
                element = (total + next_num, r_idx + 1)
                heapq.heappush(min_heap, element)
            return total
        
        # considering 1-based index
        l, r = left-1, right-1 

        # skip all nums before [left]
        for _ in range(l):
            activity()
        # account all nums from [left, right]
        res_range = (activity() % MOD for _ in range(l, r+1)) # r is inclusive

        return sum(res_range) % MOD 

l = [1,2,3,4]
s = Solution() 
s.rangeSumA2(l, 4, 1, 5)