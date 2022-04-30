# https://leetcode.com/problems/find-missing-observations/

from typing import List

def missingRolls(rolls: List[int], mean: int, n: int) -> List[int]:
    m = len(rolls)
    # nTotal := remaining
    nTotal = (mean * (n+m)) - sum(rolls)  # Expected - Emperical

    if nTotal < n or nTotal > n*6:
        return []  # cannot divide the Dice cnnts among {n} rolls successfully

    res = []
    # Greedily Fill each n-space of rolls
    while nTotal:
        rollVal = min(nTotal - n + 1, 6) # val allowed in range (1 - 6)
        nTotal -= rollVal  # deduct the {rollVal}
        res.append(rollVal) # account the {rollVal}
        n -= 1 # remaining rolls
    
    return res




def missingRolls(rolls: List[int], mean: int, n: int) -> List[int]:
    m = len(rolls) # cnt of rolls
    expectedSum = mean * (n+m)  # expected sum overall (existing + missing) observations
    empericalSum = sum(rolls)  # existing observationn sum

    remain = expectedSum - empericalSum

    if n <= remain <= n*6:
        q, r = divmod(remain, n)
        if r:
            return [q]*(n-1) + [q+r]
        else:
            return [q]*(n)
    else:
        return [] 

rolls = [3,2,4,3]
mean = 4
n = 2

rolls = [1,5,6]
mean = 3
n = 4

rolls = [1,2,3,4]
mean = 6
n = 4

ans = missingRolls(rolls, mean, n)
print(ans)
