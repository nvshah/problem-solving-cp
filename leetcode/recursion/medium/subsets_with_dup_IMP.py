# https://leetcode.com/problems/subsets-ii/

from typing import List
from collections import Counter as ctr
import itertools as it

'''
Idea : left part will search considering duplicates
       right part will search only unique combinations
'''
def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    nums.sort() # so that all duplicates are placed side by side
    size = len(nums)
    ans = []
    possible = []
    def dfs(i):
        if i >= size:
            ans.append(possible.copy())
            return

        n = nums[i]
        
        #---------
        # Search for repeated (if there exists) combinations
        # 1. pick (include) {n}
        possible.append(n)
        # for first time include all elements (repeated as well)
        dfs(i+1)

        # 2. unpick (discard) {n}
        possible.pop()

        # discard all repeated {n}
        j = i
        while j+1 < size and nums[j+1] == nums[j]:
            j += 1

        #-----------  
        # this will search unique elements combination only
        # search for Unique on RHS side only
        dfs(j+1)
    
    dfs(0)
    return ans

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

def subsetsWithDup2(nums: List[int]) -> List[List[int]]:
    nums.sort() # so that all duplicates are placed side by side
    m = ctr(nums)
    repeats = {e for e in m if m[e] > 1}
    ans = []
    
    # Find all unique combinations subsets
    uniques = subsets([*m.keys()])

    # amend the repeated elements in unique combinations
    for p in uniques:
        s = set(p)
        common = repeats & s
        diff = s - repeats
        if common:
            for c in common:
                if c in repeats:
                    for i in range(1, m[c]+1):
                        ans.append([*diff, *[c]*i])
        else:
            ans.append(p)
    
    print(ans)
    return ans 

def subsetsWithDup3(nums: List[int]) -> List[List[int]]:
    nums.sort() # so that all duplicates are placed side by side
    def dfs(p, up):
        if not up:
            return [p]
        # ! (HINT) consider repeated element as single entity
        
        f = up[0]  # first element in unprocessed list
        # 1 pick
        l = dfs([*p, f], up[1:]) # consider all the elements from unprocessed one by one
        # 2 unpick 
        *up, = it.dropwhile(lambda x: x == f, up) # ignore all the (repeatable) elements {f} from unprocessed list
        r = dfs(p, up)
        return [*l, *r]

    return dfs([], nums)

def subsetsWithDup4(nums: List[int]) -> List[List[int]]:
    nums.sort() # so that all duplicates are placed side by side
    ans = []
    p = []
    def dfs(up):
        if not up:
            ans.append(p.copy())
            return 
        # ! consider repeated element as single entity
        f = up[0]
        # 1 pick
        p.append(f)
        dfs(up[1:])
        # 2 unpick 
        p.pop()
        dfs(list(it.dropwhile(lambda x: x == f, up)))

    dfs(nums) 
    return ans

# nums = [1,2,2]
nums = [4,4,4,1,4]
#a = subsetsWithDup2(nums)
a = subsetsWithDup3(nums)
print(a)

