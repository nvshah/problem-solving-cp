#https://leetcode.com/problems/kth-distinct-string-in-an-array

'''
Counter | Generator | ISlice (take/skip)
'''

from typing import List
from collections import Counter 
from itertools import islice


def kthDistinct(arr: List[str], k: int) -> str:
    freqs = Counter(arr) 
    uniques = (e for e in freqs if freqs[e] == 1) 
    kth_element = next(islice(uniques, k-1, k), None)
    return kth_element if kth_element else ''

ans = kthDistinct(["a","b","a"], 3) 

print(ans)