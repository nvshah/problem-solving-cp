# https://leetcode.com/problems/partition-labels/
from typing import List


def partitionLabels(s: str) -> List[int]:
    ridxMap = {c: i for i,c in enumerate(s)}  # Map of char -> ridx
    res = []  
    size = 0  # Curr size of Sliding Window
    u = 0  # Upper Bound of Current Window
    for l in range(len(s)):
        size += 1  # include curr char in curr window
        # update the correct upper bound of curr Window 
        u = max(u, ridxMap[s[l]])
        # Check if Window is Explored all
        if l == u: # found a part
            res.append(size)
            size = 0
    return res 
        
s = "ababcbacadefegdehijhklij"
s = "eccbbbbdec"
print(partitionLabels(s))
