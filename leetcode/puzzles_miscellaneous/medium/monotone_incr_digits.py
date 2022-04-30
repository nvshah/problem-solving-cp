# https://leetcode.com/problems/monotone-increasing-digits/

def monotoneIncreasingDigits(n: int) -> int:
    s = str(n)
    l = len(s)
    ns = []
    i=0
    while i < l-1:
        if s[i] > s[i+1]:
            ns.append(str(int(s[i])-1))
            i += 1
            break
        ns.append(s[i])
        i += 1
    else:
        return n
    
    while i < l:
        ns.append('9')
        i += 1
    
    return int(''.join(ns))

n = 10
ans = monotoneIncreasingDigits(n)
print(ans)