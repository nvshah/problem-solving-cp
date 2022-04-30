# https://leetcode.com/problems/last-stone-weight/

from typing import List 
import heapq

def lastStoneWeight(stones: List[int]) -> int:
    ''' O(n*logn) '''
    maxHeap = [-s for s in stones]  # Hack for max-heap via min-heap
    heapq.heapify(maxHeap)

    while len(maxHeap) > 1 : # till we don't get atmost 1 stone
        first = heapq.heappop(maxHeap)   # first largest stone ie (-first)
        second = heapq.heappop(maxHeap)  # second largest stone ie (-second)

        # ideally second stone is <= first stone 
        # (but as we negate while making max-heap) so condition will also get negate
        # Thus original ~(second<=first) := second > first
        if second > first: # second stone is smaller in weight compare to first stone originally (due to `-` sign)
            heapq.heappush(maxHeap, first-second)  # ideally first is larger than second
    
    return -maxHeap[0] if maxHeap else 0
