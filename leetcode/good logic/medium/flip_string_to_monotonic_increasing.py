# https://leetcode.com/problems/flip-string-to-monotone-increasing/description/

def minFlipsMonoIncr(s: str) -> int:
    '''O(n) logic : Greedy Solution
    Try to minimize the efforts for whatever substring is explored at moment
    '''
    ones_cnt = flips = 0

    for c in s:
        if c == '0':
            flips = min(ones_cnt, flips+1) 
        else:
            ones_cnt += 1

    return flips