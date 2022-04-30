# https://leetcode.com/problems/find-median-from-data-stream/

import heapq

class MedianFinder:

    def __init__(self):
        # 2 heaps :- small (maxHeap) & large (minHeap) 
        self.small = []  # Store the first half small elements in Max Heap manner
        self.large = []  # Store the second half large elements in Min Heap manner
        

    def addNum(self, num: int) -> None:
        # 1. Push new element in small (maxHeap)
        heapq.heappush(self.small, -num)

        # 2. Make Sure every num in {small} is <= every num in {large}
        if self.small and self.large:
            r1 = -1 * self.small[0]  # largest elem from first half (small)
            r2 = self.large[0]  # smallest elem from second half (large)

            if r1 > r2: # need to move larger element to {large} side ie minHeap
                s1 = -1 * heapq.heappop(self.small) # remove element from {small}
                heapq.heappush(self.large, s1) # add value to {large}
            
        # 3. Size Invariant (UnEven)
        size_small = len(self.small)
        size_large = len(self.large)

        if size_small > size_large + 1:
            # move largest element from {small} to {large}
            small_largest_elem = -1*heapq.heappop(self.small)
            heapq.heappush(self.large, small_largest_elem)

        elif size_large > size_small + 1:
            # move smalles element from {large} to {small}
            large_smallest_elem = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*large_smallest_elem)
                

    def findMedian(self) -> float:
        size_small = len(self.small)
        size_large = len(self.large)

        if size_small > size_large:
            return -1*self.small[0]   # largest val in small (maxHeap)
        elif size_large > size_small:
            return self.large[0]      # Smallest Val in large (minHeap)
        
        # median = (largest in {small} + smallest in {large}) / 2
        return (-self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()