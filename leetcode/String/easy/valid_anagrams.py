
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    ss = set(s)
    for c in ss:
        if s.count(c) != t.count(c):
            return False
    return True