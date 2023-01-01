# https://leetcode.com/problems/remove-stones-to-minimize-the-total/
from typing import List
import heapq

def minStoneSum(piles: List[int], k: int) -> int:
    # Create MaxHeap (priority queue) for piles
    maxHp = [-p for p in piles]
    heapq.heapify(maxHp)

    while maxHp and k:
        total = -heapq.heappop(maxHp)  # Empty out Pile
        removed = total // 2   # stones to be removed
        remains = total - removed 
        if remains:
            heapq.heappush(maxHp, -remains)  # put remaining store in Pile
        k -= 1
    
    return -sum(maxHp)

piles = [5,4,9]
k = 2
ans = minStoneSum(piles, k)
print(ans)