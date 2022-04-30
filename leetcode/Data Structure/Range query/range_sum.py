# https://leetcode.com/problems/range-sum-query-immutable/

from typing import List


def lsb(n):
    return n & -n

class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = [0, *nums]
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


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)