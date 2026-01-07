# smallest-range-covering-elements-from-k-lists

from typing import List
import heapq

"""
Techniques
- k pointers
- sliding window
- Heap
"""


def smallestRange(nums: List[List[int]]) -> List[int]:
    # pointing to current range boundaries
    left = right = nums[0][0]

    # prepare heap # to start with first element from each lists
    minHeap = []  # (element, position_in_list, index_of_list)
    for i, l in enumerate(nums):
        left = min(left, l[0])
        right = max(right, l[0])
        heapq.heappush(minHeap, (l[0], 0, i))

    res = (left, right)
    while minHeap:
        _, pos, list_idx = heapq.heappop(minHeap)

        l = nums[list_idx]
        nxt = pos + 1

        if nxt == len(l):
            break

        # account new elem
        elem = l[nxt]
        heapq.heappush(minHeap, (elem, nxt, list_idx))

        # update res based on new candidates
        left = minHeap[0][0]
        right = max(right, elem)

        if right - left < res[1] - res[0]:
            res = (left, right)

    return res
