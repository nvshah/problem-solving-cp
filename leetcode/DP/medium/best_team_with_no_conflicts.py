# https://leetcode.com/problems/best-team-with-no-conflicts/description/
from typing import List
from operator import itemgetter

# IDEA1 : BOTTOM-UP DP

def bestTeamScore(scores: List[int], ages: List[int]) -> int:
    '''Idea: Bottom-Up DP'''    
    items = sorted(zip(scores,ages))
    print(items)
    # val at index i implies the bestScore possible with first i+1 players
    *dp, = map(itemgetter(0), items) 

    for i in range(1, len(dp)):
        # bestScore considering first [i+1] players
        score, age = items[i] # current player
        bestScore = score
        for j in range(i):
            if items[j][1] <= age:  # considering first j players
                bestScore = max(bestScore, score + dp[j])
        dp[i] = bestScore
    
    return max(dp)

# scores = [1,3,5,10,15]
# ages = [1,2,3,4,5]
scores = [1,3,7,3,2,4,10,7,5]
ages = [4,5,2,1,1,2,4,1,4]
ans = bestTeamScore(scores, ages)
print(ans)