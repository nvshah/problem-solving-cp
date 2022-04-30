# https://leetcode.com/problems/kth-largest-element-in-a-stream/

from typing import List
import heapq

'''
Goal :- Find the kth largest element in the array after several operation
Idea :- As we need to add for each operation So we can use heap for purpose
        because add & remove in heap requires O(logn) time
        push :- O(logn)
        pop :- O(logn)

'''
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        ''' T.C = O(nlog(n)) '''
        # O(n) times to create min heap ie smallest elem at top as a root
        heapq.heapify(nums) 
        size = len(nums)
        # ensuring the heap size boils down to k element 
        # so we can have kth largest element at top as a root
        for _ in range(size-k):
            heapq.heappop(nums)

        self.hp = nums
        self.k = k

    def add(self, val: int) -> int:
        ''' T.C = O(log(n)) '''
        if len(self.hp) < self.k:  # as there are empty seat already available
            heapq.heappush(self.hp, val)
        elif val >= self.hp[0]:  # val can take any seat in heap & root needs to be removed
            v = heapq.heapreplace(self.hp, val)
        return self.hp[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

o = KthLargest(3, [4,5,8,2])
print(o.hp)
n = o.add(3)
print(n)
n = o.add(5)
print(n)
n = o.add(10)
print(n)
n = o.add(9)
print(n)
n = o.add(4)
print(n)