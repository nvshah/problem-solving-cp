from typing import List
 
def restoreIpAddresses(s: str) -> List[str]:
    size = len(s)
    # Check Edge Condition
    if size > 12: return []

    res = []

    def backtrack(i, dots, curIp):
        if i == size and dots == 4:
            res.append(curIp[:-1])  # discarding the last 4th dot
            return 
        if dots > 4:  # Cannot cover entore number into IP address
            return 
        
        end_offset = min(i+3, size)  # end place where we can put the next dot

        for j in range(i, end_offset):  # j is the offset to place from {i}
            # place dot
            part = s[i:j+1]
            # 1. number must be lt 255
            # 2. number must not start with 0
            if int(part) <= 255 and (i == j or s[i] != '0'):
                backtrack(j+1, dots+1, curIp + part + '.')
        
    backtrack(0, 0, '')
    return res 


def restoreIpAddresses2(s: str) -> List[str]:
    N = len(s) 

    res = [] # possible ip-addresses
    cur = [] # cur dot position (permutation)

    def helper(i, k):
        '''place [k] dots in string[i:]'''
        cur_str_len = N - i 

        if cur_str_len < k+1: return # not enough places for [k] dots in cur-substr

        if k == 0: # all dots are placed
            if isValidPart(s, i, N):
                res.append(constructIpAddress(s, cur))
            return 
        
        start = i+1
        end = min(start+3, N)
        
        for j in range(start, end):
            if not isValidPart(s, i, j): break 
            cur.append(j) 
            helper(j, k-1)
            cur.pop() 
    
    helper(0, 3)
    return res 

def isValidPart(string, s, e):
    part = string[s: e]
    noLeadingZero = len(part) == 1 or part[0] != '0' 
    isValidValue = 0 <= int(part) <= 255

    return noLeadingZero and isValidValue
 
def constructIpAddress(string, dotsPos):
    charArr = list(string)
    for i in reversed(dotsPos):
        charArr.insert(i, '.')
    return ''.join(charArr)

s = "25525511135"
s = "0000"
ans = restoreIpAddresses2(s)
print(ans)
