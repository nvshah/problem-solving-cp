# https://leetcode.com/problems/isomorphic-strings/

def isIsomorphic(s: str, t: str) -> bool:
    sLen, tLen = len(s), len(t)
    
    if sLen != tLen: return False  # if 2 diff length then not possible to get t from s
    
    map = {}    # mapping of character from s -> t
    map_vals = set()  # set of vals of mapped t's character
    
    for c1, c2 in zip(s, t):   # c1 -> char of s & c2 -> char of t
        if c1 in map:
            if map[c1] != c2: return False   # s's char (ie c1) has clash of multiple mappings
        else:  
            if c2 in map_vals: return False  # t's char (ie c2) is already mapped
            map[c1] = c2
            map_vals.add(c2)
    return True