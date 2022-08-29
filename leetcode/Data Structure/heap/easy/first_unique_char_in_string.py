# https://leetcode.com/problems/first-unique-character-in-a-string/submissions/

from collections import defaultdict
import heapq


def firstUniqChar(s: str) -> int:
    d = defaultdict(lambda : (0, -1))
    
    for i, c  in reversed([*enumerate(s)]):
        d[c] = (d[c][0] + 1, i)
    
    h = list(d.values())
    heapq.heapify(h)
    
    if h[0][0] == 1: return h[0][1]
    
    return -1

def firstUniqChar2(s: str) -> int:
    # d = {}

    # single = set()
    # many = set()

    # for i, c in enumerate(s):
    #     if c not in d:
    #         d[c] = i         
    #     else:
    #         many
    #         del d[c]
    
    # return d.values()[0]

