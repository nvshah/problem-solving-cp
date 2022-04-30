# https://leetcode.com/problems/convert-to-base-2/
from math import ceil

def baseNeg2(n: int) -> str:
    if n == 0: return "0"
    res = []
    while n:
        # ceil -> because n can be -ve & we want it close to +ve as much as possible
        # remainder -> need to be +ve always So we are settingg quotient accordingly via use of ciel()
        n, r = ceil(n/-2), abs(n%2)  
        #print(n, r)
        res.append(str(r))

    return ''.join(res[::-1])


n = 2
n = 3
#n = 4
ans = baseNeg2(n)
print(ans)
