# https://leetcode.com/problems/combination-sum-ii/

from typing import List


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    sNominee = sorted(candidates)
    currComb = []
    res = []
    size = len(candidates)
    def dfs(i, currSum):
        if currSum == target:
            res.append(currComb.copy())
            return
        if i == size or currSum > target:
            return 

        v = sNominee[i]

        # 1. Allow duplicates in Left Part
        currComb.append(v)
        dfs(i+1, currSum+v)

        # 2. BackTrack
        currComb.pop()

        # 3. Skip all duplicates in Right Part
        j = i + 1  # {j} -> points to next nnominee of current one ie {i}
        while j < size and sNominee[j-1] == sNominee[j]:
            j += 1
        dfs(j, currSum)
    
    dfs(0, 0)
    return res 

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    currComb = []
    res = []
    size = len(candidates)

    def dfs(i, currSum):
        '''
        i :- pos from where to search the element
        currSum :- sum of currently selected element
        '''
        if currSum == target:
            res.append(currComb.copy())
            return
        if currSum > target:
            return

        prev = -1 
        for j in range(i, size):
            v = candidates[i]
            if v == prev:
                continue

            currComb.append(v)
            dfs(i+1, currSum+v)
            currComb.pop()

            prev = v
    
    dfs(0, 0)
    return res 

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    res = []

    def backtrack(curr, pos, target):
        if target == 0:
            res.append(curr.copy())
            return
        if target < 0:  # Exceeded than what required
            return

        prev = -1 
        for i in range(pos, len(candidates)):
            v = candidates[i]
            if v == prev:  # Skip already explored candidate 
                continue

            curr.append(v)  # Explore (allowing duplicates for one time only)
            backtrack(curr, i+1, target-v)
            curr.pop()    # BackTrack

            prev = v
    
    backtrack([], 0, target)
    return res 

candidates = [10,1,2,7,6,1,5]
target = 8

ans = combinationSum2(candidates, target)
print(ans)
