# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List
from itertools import product

def letterCombinations(digits: str) -> List[str]:
    '''
        All Combination = Cartesian Product need to be found
        approach via Decision Tree & Recursion
        number of level = length of digits
        All the possible ans will be found at each Leaf Node (via backtracking to root)
    '''
    if not digits:
        return []
    
    m = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    #size = len(digits)
    ans = []

    return map(lambda l : ''.join(l), product(*map(m.__getitem__, digits)))