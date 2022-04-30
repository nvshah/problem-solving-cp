# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

from typing import List
from itertools import islice

def minDominoRotations(tops: List[int], bottoms: List[int]) -> int:
    '''
    O(n)
    Idea :- Any Pair (top-bottom) either top or bottom needs to be present amongst all pairs (either side)
    '''
    size = len(tops)
    # lets consider pivot = first pair
    for target in (tops[0], bottoms[0]):
        missTop = missBottom = 0
        # Skip first comparision 
        for i, pair in enumerate(zip(tops, bottoms)):
            print(i, pair)
            if target not in pair:  # pair = (top, bottom)
                break   # as top & bottom not match with {target} so all elem cannot be made {target}
            
            missTop += (pair[0] != target)
            missBottom += (pair[1] != target)

            if i == size-1:  # reach last index
                return min(missTop, missBottom)
    return -1

tops = [2,1,2,4,2,2]
bottoms = [5,2,6,2,3,2]

# Case 2
tops = [2,5,5,5,5]
bottoms = [5,1,1,1,1]

a = minDominoRotations(tops, bottoms)
print('ans :', a)