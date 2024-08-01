# https://leetcode.com/problems/maximum-number-of-coins-you-can-get
from typing import List 

# O(nlogn) time | O(1) space
def maxCoins(piles: List[int]) -> int:
    '''
    sort coins
    # now first (N//3) will be taken by Bob (ie least val)
    # I will take coin in alternate fashion from (N//3) to maximise my Pile
    '''
    N = len(piles)
    piles.sort()
    return sum(piles[i] for i in range(N//3, N, 2)) 

