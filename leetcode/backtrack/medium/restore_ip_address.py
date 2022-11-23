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

s = "25525511135"
restoreIpAddresses(s)
