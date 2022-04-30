# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List
import itertools as it
from string import ascii_lowercase as letters

m = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

def letterCombinations(digits: str) -> List[str]:
    '''
        All Combination ie Cartesian Product need to be found
        approach via Decision Tree & Recursion
        number of level = lenght of digits

        All the possible ans will be found at each Leaf Node (via backtracking to root)
    '''

    if not digits:
        return []

    size = len(digits)
    ans = []
    
    def combine(i, currStr):
        '''
        look for digit at i characters to combinne with current String
        currStr is meant for backtracking 
        '''

        # if i == size
        #if len(currStr) == size:  # reach the leaf of DT
        if i == size: # reach the leaf of DT
            ans.append(currStr)
            return
        
        digit = digits[i]
        for ch in m[digit]: # find all the combinations for this {digit}
            combine(i+1, currStr+ch)

    combine(0, '')

    return ans

def letterCombinations2(digits: str) -> List[str]:
    return map(lambda l : ''.join(l), it.product(*map(m.__getitem__, digits)))

def letterCombinations3(digits: str) -> List[str]:
    m = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    return map(lambda l : ''.join(l), it.product(*map(m.__getitem__, map(int, digits))))

def letterCombinations4(digits: str) -> List[str]:
    '''
     Deprecated old Answer
    '''
    ans = []
    def pad(p, up):
        '''
            p: processed
            up: unprocessed
        '''
        if not up:
            ans.append(p)
            return
        
        # get the first digit
        digit = int(up[0])
        l = (digit-1)*3
        u = l + 3
        for c in letters[l:u]:
            pad(p+c, up[1:])

    pad('', digits)
    return ans


# l1 = [1,2,3]
# l2 = [4,5,6]
# l3 = [7,8,9,10]

# *a, = it.product(l1,l2,l3)

d = "23"
print(letterCombinations(d))

print(letterCombinations4(d))
