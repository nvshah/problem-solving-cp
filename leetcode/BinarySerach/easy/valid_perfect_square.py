# https://leetcode.com/problems/valid-perfect-square/
from bisect import bisect

# BInary Search
def isPerfectSquare(num: int) -> bool:
    if num == 1: return True 
    #valids = [n for n in range(1, num//2)]
    s, e = 1, num//2
    while s <= e:
        m = (s + e) // 2
        sq = m*m
        if sq == num:
            return True 
        elif sq < num:
            s = m+1
        else:
            e = m-1 
    return False