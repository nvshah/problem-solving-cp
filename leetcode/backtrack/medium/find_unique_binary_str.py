# https://leetcode.com/problems/find-unique-binary-string/submissions/
from typing import List
from itertools import permutations

def findDifferentBinaryString1(nums: List[str]) -> str:
    ''' Brute Force'''
    l = len(nums)
    s = '0'*l + '1'*l
    setNums = set(nums)
    p = permutations(s, l)
    for b in p:
        st = ''.join(b)
        if st not in setNums:
            return st

def findDifferentBinaryString2(nums: List[str]) -> str:
    l = len(nums)
    numSet = {*nums}
    def backtrack(d, string):
        if d == l: # max depth
            if string not in numSet:
                return string 
            else: 
                return None
        
        # # 0
        # r = backtrack(d+1, string+'0')
        # if r:
        #     return r

        # # 1 
        # r = backtrack(d+1, string+'1')
        # if r:
        #     return r

        # Explore each one by one
        for b in ('0', '1'):
            r = backtrack(d+1, string+b)
            if r: return r
        
        #return ''

    return backtrack(0, '')

nums = ["01","10"]
print(findDifferentBinaryString2(nums))
