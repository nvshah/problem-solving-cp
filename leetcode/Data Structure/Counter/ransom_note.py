# https://leetcode.com/problems/ransom-note/

from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    r = Counter(ransomNote)
    m = Counter(magazine)
    
    return all(map(lambda k: r[k] <= m[k], r))