# https://leetcode.com/problems/bag-of-tokens/
from collections import deque
from collections import List

def bagOfTokensScore(tokens: List[int], power: int) -> int:
    que = deque(sorted(tokens)) # queue of candidate tokens
    score = 0
    max_score = 0
    while que:
        if power >= que[0]:
            # smallest token (Greedy -> to get Score)
            token = que.popleft()
            power -= token
            score += 1
            # Max Score is only affected when we increase score
            max_score = max(score, max_score)
        elif score > 0:
            # largest token (Greedy -> to get Power)
            token = que.pop()
            score -= 1
            power += token 
        else:
            # Neither power nor score in possession
            break
        
    return max_score