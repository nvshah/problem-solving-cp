# https://leetcode.com/problems/hand-of-straights/

import heapq
from typing import List
from collections import Counter


def isNStraightHand(hand: List[int], groupSize: int) -> bool:

    if len(hand) % groupSize != 0: return False

    # 1. frequency
    freqs = Counter(hand)

    # 2. Min Heap
    minHeap = [*freqs.keys()]
    heapq.heapify(minHeap)

    while minHeap:
        # first member in current group forming
        first = minHeap[0]

        for i in range(first, first+groupSize):
            if i not in freqs:
                return False 
            # use this number as member {i} in current group forming
            freqs[i] -= 1  
            if freqs[i] == 0:
                # then this {i} must be the minimum among rest (ie present at top of min-heap)
                if i != minHeap[0]:
                    return False 
                # We can pop this {i} as its no more available for forming future groups
                heapq.heappop(minHeap)
        
    return True


hand = [1,2,3,6,2,3,4,7,8]
size = 3

ans = isNStraightHand(hand, size)
print(ans)
