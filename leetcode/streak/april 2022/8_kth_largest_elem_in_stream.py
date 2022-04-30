import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
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
        if len(self.hp) < self.k:  # as there are empty seat already available
            heapq.heappush(self.hp, val)
        elif val >= self.hp[0]:  # val can take any seat in heap & root needs to be removed
            heapq.heapreplace(self.hp, val)
        return self.hp[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)