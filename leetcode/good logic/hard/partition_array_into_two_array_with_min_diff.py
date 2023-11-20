# https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/
from typing import List
from itertools import combinations
from bisect import bisect

def findAllSums(nums):
    res = {sum(nums)}

    for i in range(1, len(nums)):
        res.update({sum(sub) for sub in combinations(nums, i)})
    
    return res 

def minAbsDifference(nums: List[int], goal: int) -> int:
    '''Meet in the Middle'''
    n = len(nums)
    m = n // 2
    sum1 = findAllSums(nums[:m])
    sum2 = findAllSums(nums[m:])

    if goal in sum1 or goal in sum2: return 0

    sum2 = sorted(sum2)

    ans = abs(goal) 

    n2 = len(sum2)
    for s1 in sum1:
        t = goal-s1 
        #if t == 0: return 0

        i = bisect(sum2, t) # Find pos for {t}

        # check two nearest value ie after & before
        if i < n2: # After
            diff = abs(sum2[i] - t)
            if diff == 0: return 0
            ans = min(ans, diff)
        
        if i > 0: # before
            diff = abs(t - sum2[i-1])
            if diff == 0: return 0
            ans = min(ans, diff)

    return ans 

def minimumDifference(nums: List[int]) -> int:
    if(len(nums) <= 3):
        m = len(nums) // 2
        return abs(sum(nums[:m]) - sum(nums[m:]))
    total = sum(nums) 
    target1 = total // 2
    
    missing1 = minAbsDifference(nums, target1) 

    bag1 = target1-missing1 
    bag2 = total-bag1 
    
    return bag2-bag1

# TEST ---

def testCaseInvalid():
    nums = [76,8,45,20,74,84,28,1] # WRONG CASE IN LEETCODE | Expected: 2 but actually its 0
    s1 = [76, 8, 84] 
    s2 = [45, 20, 74, 28, 1]
    ans = minimumDifference(nums)
    matchAns = sum(s2) - sum(s1)

#nums = [3,9,7,3]
nums = [-36, 36]
nums = [2,-1,0,4,-2,-9]
nums = [-2, 0, 2]

print(ans)
