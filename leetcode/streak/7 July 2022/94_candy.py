# https://leetcode.com/problems/candy/

from typing import List


def candy(ratings: List[int]) -> int:
    n = len(ratings)
    assigned = [1]*n
    
    # Left to Right
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            assigned[i] = assigned[i-1]+1
    
    # Right to Left
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            assigned[i] = max(assigned[i], assigned[i+1]+1)
    
    return sum(assigned)