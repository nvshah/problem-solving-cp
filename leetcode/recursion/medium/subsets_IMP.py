# https://leetcode.com/problems/subsets/

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    '''
        Use Recursion to obtain sublists
        When you encounter the Leaf Node in DT, you will get one of possible sublist
    '''

    res = []
    subset = []  # temp list store the current sublist members
    size = len(nums)

    def dfs(i):
        '''
         i -> pos at where from we need to look for subsets
        '''
        if i == size:    # Reach to the Leaf of DT where you get one of possible subset
            res.append(subset.copy())
            return 
        
        # Take num[i]
        subset.append(nums[i])
        dfs(i+1)

        # Check for subsets possibilities discarding the nums[i]
        subset.pop() 
        dfs(i+1)
    
    dfs(0)
    return res


def subsets2(nums: List[int]) -> List[List[int]]:
    '''
        Use Recursion to obtain sublists
        When you encounter the Leaf Node in DT, you will get one of possible sublist
    '''
    def dfs(p, up):
        '''
         p -> processed
         up -> unprocessed
        '''
        if not up:    # Reach to the Leaf of DT where you get one of possible subset
            return [p]
        
        f = up[0]     # first 
        remains = up[1:] # to be processed in future
        l = dfs([*p, f], remains) # include first
        r = dfs(p, remains) # exclude first

        return [*l, *r]
    
    return dfs([], nums)

