# https://leetcode.com/problems/reduce-array-size-to-the-half/

from collections import Counter
import heapq
from typing import List

'''
Logic

Steps :
1. Find the frequencies for each element (via Counter)
2. Create MaxHeap for Frequenceis Count only (via heapq)
3. pop each count until it reaches half
'''


def minSetSize(arr: List[int]) -> int:
    # 1. Step 1
    ctr = Counter(arr)
    # 2. Step 2
    hp = [-cnt for cnt in ctr.values()]  # maxheap
    heapq.heapify(hp)
    
    cnt = len(arr)   # initial count in array
    half = cnt // 2  
    
    ans = 0  # removed unique integers
    
    while cnt > half:
        f = -heapq.heappop(hp)
        cnt -= f
        ans += 1
        
    return ans