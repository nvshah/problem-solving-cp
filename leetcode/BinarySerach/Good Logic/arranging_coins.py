# https://leetcode.com/problems/arranging-coins/

def arrangeCoins(n: int) -> int:
    l, r = 1, n
    ans = n
    while l <= r:
        m = (l+r) // 2
        msum = m*(m+1) // 2  # Sum of 1 -> m
        if msum == n: # all the stairs are equipped
            return m 
        if msum > n:  # more coins than available (so need to reduce stairs level)
            r = m-1
        else: 
            ans = m   # found 1 ans
            l = m+1   # search for more (greedy)
    return ans