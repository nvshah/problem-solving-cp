# https://leetcode.com/problems/ugly-number/

def isUgly(n: int) -> bool:
    if n <= 0: return False
        
    for p in [2, 3, 5]:
        while n % p == 0:
            n //= p
    
    return n == 1  # broken down by only 2, 3, successfully