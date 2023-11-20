# https://www.codingninjas.com/studio/problems/subset-sum-equal-to-k_1550954


def subsetSumToK(n, k, arr):
    '''DP Tabulation'''
    dp = [1, *[0]*(k+1)]  # targets possibility
    
    for i in range(n):
        num = arr[i]
        newDp = list(dp) # this will cover exclude num implicitly
        for t in range(num, k+1): # include num cases
            if dp[t] == 0:  # previously target {t} is not founded 
                newDp[t] = dp[t-num] # so check if {num} can contribute in finding {t}
        
        if newDp[k] == 1: return True  # found subset for {k}
        dp = newDp 
    
    return False
            



def subsetSumToK2(n, k, arr):
    '''Set DP'''
    dp = {0} # possible sums of subsets
    for num in arr:
        temp = set(dp)
        for p in dp:
            total = p + num 
            if total == k: return True 
            if total < k:
                temp.add(total) 
        dp = temp
    return False 

def subsetSumToK1(n, k, arr):
    '''DP-Memoization-Recursion'''
    dp = [1, *[0]*(k+1)] # target possibilities

    for i in range(n):
        num = arr[i]
        newDp = list(dp)
        for target in range(1, k+1):
            take = 0
            if num <= target:
                take = dp[target-num]
            notTake = dp[target]

            newDp[target] = take | notTake
        
        if newDp[k] == 1: return True 
        dp = newDp 

def subsetSumToK1(n, k, arr):
    '''DP-Memoization-Recursion'''
    cache = {}

    def explore(i, target):

        if target == 0: return True 
        if i == n: return False 
        #if target < 0: return False # not possible

        if (i, target) in cache: 
            return cache[(i, target)]

        # include or exclude array[i]
        #if arr[i] <= target:
        #possible = explore(i+1, target-arr[i]) or explore(i+1, target)

        # not-take 
        possible = explore(i+1, target)
        if arr[i] <= target:
            # Take 
            possible = possible or explore(i+1, target-arr[i])

        cache[(i, target)] = v = possible
        return v 
    
    return explore(0, k)


ans = subsetSumToK(10, 172, [8, 59, 58, 79, 44, 7, 65, 69, 60, 51 ])
    