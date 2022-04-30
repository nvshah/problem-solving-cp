# https://leetcode.com/problems/fair-candy-swap/

from typing import List
from itertools import product


def fairCandySwap(aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
    a = sum(aliceSizes)
    b = sum(bobSizes)
    gap = (a-b) // 2
    # for s1, s2 in product(aliceSizes, bobSizes):
    #     if s1 - s2 == gap:
    #         return [s1, s2]
    for s1 in aliceSizes:
        s2 = s1 - gap
        if s2 in bobSizes:
            return [s1, s2]

aliceSizes = [1,1] 
bobSizes = [2,2] 

# aliceSizes = [1,1]
# bobSizes = [2,2]

# aliceSizes = [2]
# bobSizes = [1,3]

# aliceSizes = [1,2,5] 
# bobSizes = [2,4]

ans = fairCandySwap(aliceSizes, bobSizes)

print(ans)
