# https://www.codingninjas.com/studio/problems/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum_842494

from typing import List

def minSubsetSumDifference2(arr: List[str], n: int) -> int:
    '''DP'''
    '''This is not passing all test cases'''
    #N = len(arr)
    total = sum(arr)
    target = total // 2 
    
    dp = [0]*(target+1)

    for num in arr:
        newDp = list(dp)
        for t in range(num, target+1):
            if num+dp[t-num] <= target:
                newDp[t] = max(dp[t], num+dp[t-num])
        
        if newDp[target] == target: return 0 
        dp = newDp 
    
    return total - 2*dp[target]

def minSubsetSumDifference(arr: List[str], n: int) -> int:
    N = len(arr)
    total = sum(arr)
    target = total // 2 
    
    cache = {}

    def explore(i, val):
        '''Return nearest achievable val to target'''
        if val == target: return target 
        if val > target: return 0
        if i == N: return val

        if (i, val) in cache: return cache[(i, val)]

        # not take
        notTake = explore(i+1, val)
        take = explore(i+1, val + arr[i])
        
        cache[(i, val)] = v = max(take, notTake)
        return v 
    
    firstBag = explore(0, 0)
    secondBag = total - firstBag 

    return secondBag - firstBag