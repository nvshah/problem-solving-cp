#! https://leetcode.com/problems/climbing-stairs/

'''
Logic ->

climbStair (n) = fibonacci (n + 1)

consider fibonacci series :- 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
eg

climbStairs (2) = fibonacci (3) = 2
climbStairs (3) = fibonacci (4) = 3
climbStairs (5) = fibonacci (6) = 8
climbStairs (7) = fibonacci (8) = 21

'''

from functools import reduce
from operator import add

def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    f = s = 1
    for _ in range(n-1):
        f, s = s, f + s 
    return s

ways = climbStairs(6)
print(ways)
