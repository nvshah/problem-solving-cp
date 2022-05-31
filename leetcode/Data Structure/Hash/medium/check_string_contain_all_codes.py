# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

def hasAllCodes(s: str, k: int) -> bool:
    hs = set() # hash set
    for i in range(len(s)-k+1):
        p = s[i: i+k]
        hs.add(p)
        if len(hs) == 2**k: return True
    
    return False