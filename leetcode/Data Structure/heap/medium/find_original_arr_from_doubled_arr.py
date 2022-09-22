# https://leetcode.com/problems/find-original-array-from-doubled-array/

from typing import List 
import heapq
from collections import Counter 

# Currently Working Soln
def findOriginalArray1(changed: List[int]) -> List[int]:
    n = len(changed)
    if n % 2 != 0: return []  # needs double sizeed array
    half = n // 2
    
    freqs = Counter(changed) 
    heapq.heapify(changed) 
    ans = []  # original
    cnt = 0  # # original element count tracking
    
    while cnt != half:
        e = heapq.heappop(changed)  # original element speculated
        if freqs[e] == 0: continue  # Accounted as a Double
        freqs[e] -= 1
        cnt += 1 # Consider
        d = e*2  # double element corresp to speculated original element
        if d not in freqs or freqs[d] == 0:
            return [] 
        freqs[d] -= 1
        ans.append(e)  # valid original element found

    return ans 

def findOriginalArray2(changed: List[int]) -> List[int]:
    '''TODO: Not Complete Code'''
    n = len(changed)
    if n % 2 != 0: return []  # needs double sizeed array
    
    # Split inot Even | Odd
    odd, even = [], []
    for n in changed:
        if n%2 == 0:
            even.append(n)
        else:
            odd.append(n)
    
    heapq.heapify(odd)
    heapq.heapify(even)

    while odd:
        e = heapq.heappop(odd)
        d = heapq.heappop(even)

        if d != e*2:
            return []
    
    cnts = Counter(even)
    keys = cnts.keys()

    rem = len(keys)
    if rem % 2 != 0: return []

    heapq.heapify(keys)


l = [0,3,2,4,6,0]
a = findOriginalArray1(l) 
print(a)