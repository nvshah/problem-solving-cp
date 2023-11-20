# https://leetcode.com/problems/find-the-winner-of-an-array-game/
from typing import List 

def getWinner(arr: List[int], k: int) -> int:
    winner = arr[0]
    gamesWon = 0

    for n in arr[1:]:
        if n > winner:
            winner = n 
            gamesWon = 0
        gamesWon += 1
        if gamesWon == k: return winner 
    
    return winner 