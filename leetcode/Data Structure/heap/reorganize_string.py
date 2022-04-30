# https://leetcode.com/problems/reorganize-string/

from typing import Counter
from itertools import accumulate
import operator

import heapq

'''
Idea :- create Heap DS where we track character with max-cnt at present (each time)
        until entire string is traversed
'''

def reorganizeString(s: str) -> str:
    # 1. Find the count of each characters
    cnts = Counter(s)

    # 2. Inorder to create max heap need to take negative of each count
    #    -(max) = min
    #    Thus in min heap later min element will represent the character with max-cnt at moment

    freqs = [(-cnt, char) for char, cnt in cnts.items()]

    # 3. Create Min Heap of -ve cnts = Max Heap of +ve cnts
    #! Here for heapq ds, there is no key param to take decision via manipulation
    #  So hack is to provide tuple with custom param as first one
    #  (cnt, char) so heapq will take decision based on cnt comparision for each element
    heapq.heapify(freqs)

    # Now char with max count is at top

    res = ''

    # 4. track the last character of reorganized string (inorder to avoid same adjacent character)
    prev = (0, '')  # last freq & char that was used in the reorganized string

    while freqs:
        # take the character with max count at present (in heap)

        # most freq, except prev
        cnt, char = heapq.heappop(freqs)
        res += char  # add the character in resulted string
        cnt += 1     # decrease the cnt of character (as -ve cnt are stored so its done +=)

        if prev[0] != 0: # if there is any prev char it can now participate in string formation
            heapq.heappush(freqs, prev)
        
        prev = cnt, char

    if prev[0] == 0:
        return res 
    else:
        return ''

s = "aab"
s = "aabab"
print(reorganizeString(s))

        
            
        

        

        




    
    