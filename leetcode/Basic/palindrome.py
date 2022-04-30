# https://leetcode.com/problems/palindrome-number/

import math

def isPalindrome(x: int) -> bool:
    if x < 0: return False
    if x == 0: return True
    #if not x % 10: return False
    t_x = x
    i = r_x = 0
    while t_x > 0:
        t_x, m = divmod(t_x, 10)
        r_x = r_x * 10 + m
        i += 1
        print(r_x)
    return x == r_x
    
n = 10
print(isPalindrome(n))
