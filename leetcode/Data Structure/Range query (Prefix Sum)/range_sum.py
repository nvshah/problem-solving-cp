# https://leetcode.com/problems/range-sum-query-immutable/

from typing import List
from itertools import accumulate


def lsb(n):
    return n & -n

# SOLUTION 1 - Fenwick Tree
class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = [0, *nums]  # Fenwick Tree (ie Binary Indexed Tree BIT)
        self.size = len(nums)
        
        for i in range(1, self.size+1):
            j = i + lsb(i)  # update dependent index of i -> j
            if j <= self.size:
                self.tree[j] += self.tree[i]
                
    def sumPrefix(self, u):
        total = 0
        i = u+1   # 1 based indexing so.
        while i > 0:
            total += self.tree[i]
            i -= lsb(i)
        return total
        
    def sumRange(self, left: int, right: int) -> int:
        return self.sumPrefix(right) - self.sumPrefix(left-1)
    
# SOLUTION 2 - Prefix Sum
class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = [*accumulate(nums)]
        
    def sumRange(self, left: int, right: int) -> int:
        if left == 0: return self.prefix[right]
        return self.prefix[right] - self.prefix[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)