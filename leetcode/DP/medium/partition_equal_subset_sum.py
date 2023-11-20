# https://leetcode.com/problems/partition-equal-subset-sum/description/
from typing import List 

import subset_sum_equals_k as helper

def canPartition(nums: List[int]) -> bool:
    total = sum(nums)
    
    if total & 1: 
        return False  # Odd
    
    target = total // 2
    # all possible totals of diff subset combinations
    allPossibleTotals = {0} # when none of nums included in subset

    for n in nums:
        temp = set(allPossibleTotals)
        for p in allPossibleTotals:
            c = p + n 
            if c == target:
                return True 
            if c < target:
                temp.add(c)
        allPossibleTotals = temp 
    
    return False 

def canPartition1(nums: List[int]) -> bool:
    '''Top-Down Memoization'''
    total = sum(nums)
    
    if total & 1: 
        return False  # Odd
    
    target = total // 2
    N = len(nums)

    cache = {}

    def dfs(i, target):
        if target == 0: return True 
        if i == N: return False 
        if target < 0: return False 

        if (i, target) in cache: 
            return cache[(i, target)]
        
        incl = dfs(i+1, target-nums[i])
        excl = dfs(i+1, target)

        cache[(i, target)] = v = incl or excl 
        return v 
    
    return dfs(0, target)

def canPartition2(nums: List[int]) -> bool:
    '''Bottom-UP Tabular DP'''
    total = sum(nums)
    
    if total & 1: 
        return False  # Odd
    
    target = total // 2
    N = len(nums)

    dp = [1, *[0]*target] # prev row

    for i in range(N, 0, -1):
        newDp = [1, *[0]*target]
        
        for j in range(1, target):
            incl = 0
            if nums[i] <= target:
                incl = dp[target-nums[i]]
            excl = dp[target]
            newDp[j] = incl | excl

        dp = newDp

    return dp[target] == 1

def canPartition3(nums: List[int]) -> bool:
    '''Bottom-UP Tabular DP'''
    total = sum(nums)
    
    if total & 1: 
        return False  # Odd
    
    target = total // 2
    N = len(nums)

    return helper.subsetSumToK(N, target, nums)

