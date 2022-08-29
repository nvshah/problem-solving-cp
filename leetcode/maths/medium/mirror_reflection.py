# https://leetcode.com/problems/mirror-reflection/
import math

'''
Concepts :
Relatively Prime
Mirror Reflection & Intercepts

p * m = q * n
We need to find m & n accordingly

'''

def mirrorReflection(p: int, q: int) -> int:
    '''
    need to find m & n s.t  p * m = q * n  
    '''
    lcm = math.lcm(p, q)
    m = lcm // p 
    n = lcm // q 

    # 1. Even total q's
    if n % 2 == 0: 
        return 2   # North-West (Top-Left) Corner
    # 2. Odd total q's
    elif m % 2 == 0:
        # In Mirror world so 
        return 0 # South-East (Bottom-Right) Corner
    else:
        # In Real World so 
        return 1 # North-East (Top-Right) Corner

p, q = 2, 1
a = mirrorReflection(p, q)
print(a)