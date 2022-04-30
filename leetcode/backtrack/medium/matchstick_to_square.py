# https://leetcode.com/problems/matchsticks-to-square/

from ast import List
from audioop import reverse


def makesquare(matchsticks: List[int]) -> bool:
    n = len(matchsticks)
    side, remain = divmod(sum(matchsticks), 4)

    if remain: return False 

    # sorting the macthsticks in descending order so that we avoid building DT if any of sticks is larger than side
    matchsticks.sort(reverse=True)

    def backtrack(i, t, r, b, l):
        if (t > side) or (r > side) or (b > side) or (l > side):
            return False
        if i == n: # all mmatchsticks are used
            return t == r == b == l == side

        v = matchsticks[i]

        if backtrack(i+1, t+v, r, b, l): return True
        if backtrack(i+1, t, r+v, b, l): return True
        if backtrack(i+1, t, r, b+v, l): return True
        if backtrack(i+1, t, r, b, l+v): return True

        return False

    return backtrack(0, 0, 0, 0, 0)

def makesquare(matchsticks: List[int]) -> bool:
    ''' O(4^n) '''
    n = len(matchsticks)
    sideLen, remain = divmod(sum(matchsticks), 4)

    if remain: return False 

    sides = [0] * 4

    # sorting the macthsticks in descending order so that we avoid building DT if any of sticks is larger than side
    matchsticks.sort(reverse=True)

    def backtrack(i):
        if i == n: # all mmatchsticks are used
            return True

        v = matchsticks[i]

        for j in range(4):
            if sides[j] + v <= sideLen:
                sides[j] += v  # explore
                if backtrack(i): return True
                sides[j] -= v  # BackTrack

        return False

    return backtrack(0)
