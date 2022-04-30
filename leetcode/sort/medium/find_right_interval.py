# https://leetcode.com/problems/find-right-interval/

from typing import List


def findRightInterval(intervals: List[List[int]]) -> List[int]:
    l = len(intervals)
    if l == 1: 
        return [-1]
    ans = [0] * l
    # i_i = enumerate(intervals)
    # i_i_s = sorted(i_i, key=lambda x: x[1][1])
    s_i = sorted(range(l), key = lambda x: intervals[x][1] / intervals[x][0])
    for i in range(len(s_i)-1):
        c, n = s_i[i], s_i[i+1] 
        if intervals[n][0] >= intervals[c][1]:
            ans[c] = n
        else:
            ans[c] = -1
    ans[s_i[-1]] = -1  # for last interval -1
    return ans

intervals = [[1,2]]
intervals = [[3,4],[2,3],[1,2]]
intervals = [[1,4],[2,3],[3,4]]
print(findRightInterval(intervals))

    

