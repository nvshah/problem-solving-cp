# https://leetcode.com/problems/optimal-partition-of-string/

def partitionString(s: str) -> int:
    charSet = set()
    parts = 1  # Entire string contains unique character

    for c in s:
        if c in charSet:
            # new part found
            parts += 1
            charSet.clear()
        charSet.add(c)
    return parts

