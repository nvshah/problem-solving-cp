# https://leetcode.com/problems/target-sum/

from typing import List


def findTargetSumWays(nums: List[int], target: int) -> int:
    '''
        Idea : Cache + Recursion = DP logic (Decision Tree Way but modified)
    '''
    dp = {} # cache
    def explore(i=0, cum_sum=0):
        '''
            Explore from ith idx 
            cum_sum is sum till ith idx
        '''
        if i == len(nums): # all nums are explored
            return 1 if target == cum_sum else 0
        if (i, cum_sum) in dp:
            return dp[(i, cum_sum)]
        # 2 options for given digit either add it or subtract it
        dp[(i, cum_sum)] = v = explore(i+1, cum_sum + nums[i]) + explore(i+1, cum_sum - nums[i])
        return v

    return explore()

nums = [1,1,1,1,1]
target = 3

nums = [1]
target = 1

nums = [44,20,38,6,2,47,18,50,41,38,32,24,38,38,30,5,26,15,37,35]
target = 44


ans = findTargetSumWays(nums, target) # 5

print(ans)




