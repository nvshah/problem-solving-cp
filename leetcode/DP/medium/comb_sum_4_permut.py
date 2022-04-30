# https://leetcode.com/problems/combination-sum-iv/

from typing import List
from math import factorial, prod
from collections import Counter
from functools import reduce
from operator import mul


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    '''
        Approach using Pure Recursion not DP
    '''
    ans = []

    def explore(i, nominees, curr_sum):
        '''
            i : pointer to current head starts from left -> right
            nominees : currently selected elements
            curr_sum : sum of all nominees
        '''
        if curr_sum == target:  # found a combination
            ans.append(nominees.copy())
            return
        if (curr_sum > target) or (i == len(candidates)):  # explored all combinations
            return 
        
        # decision 1 :  include i in nominees & explore a combination
        v = candidates[i]
        nominees.append(v)
        explore(i, nominees, curr_sum + v)  # as i is included so curr_sum also changes
        # decision 2 :  exclude i in nominees & explore a combination
        nominees.pop()
        explore(i+1, nominees, curr_sum)

    explore(0, [], 0)
    return ans

def combinationSum4_a1(nums: List[int], target: int) -> int:
    '''
        Return all permutation of possibility
    '''
    comb = combinationSum(nums, target)
    print(comb)
    ways = 0

    for c in comb:
        l = len(c)
        s = len(set(c))
        if l != s :
            f = [factorial(n) for n in Counter(c).values()]
            d = prod(f)
            ways += factorial(l) // d 
        else:
            ways += factorial(l)
        print(ways)
    return ways 

def combinationSum4(nums: List[int], target: int) -> int:
    '''
        Return all permutation of possibility Using Bottom-Up DP
        (Filling the DP table Column Wise)
    '''
    dp = {0:1}  # for sum of 0 there is only 1 way

    for i in range(1, target+1):
        dp[i] = 0 # assume there is no way initially
        for n in nums:
            dp[i] += dp.get(i-n, 0) # if not exists then 0

    return dp[target]

nums = [1,2,3]
target = 4
print(combinationSum4(nums, target))
