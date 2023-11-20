# https://leetcode.com/problems/closest-subsequence-sum/description/
from typing import List
from bisect import bisect
from itertools import combinations

'''
#### Intuition
As all combinations will take too much space so divide the problem in halves & solve inorder to reduce space usage at a time
'''

def minAbsDifference(nums: List[int], goal: int) -> int:
    '''Memory Limit Exception'''
    allSums = {0}
    ans = abs(goal)
    for num in nums:
        temp = {*allSums}
        for n in allSums:
            temp.add(n+num)
            ans = min(ans, abs((n+num)-goal))
        allSums = temp  

    return ans 

def findAllSums(nums):
    res = {0, sum(nums)}

    for i in range(1, len(nums)):
        res.update({sum(sub) for sub in combinations(nums, i)})
    
    return res 

def findAllSums2(nums):
    n = len(nums)
    res = {}
    def explore(i, total):
        if i == n: 
            res.add(total)
            return 

        explore(i+1, total+nums[i])
        explore(i+1, total)
    return res 


def minAbsDifference1(nums: List[int], goal: int) -> int:
    '''Meet in the Middle'''
    n = len(nums)
    m = n // 2
    sum1 = list(findAllSums(nums[:m]))
    sum2 = sorted(findAllSums(nums[m:]))

    ans = abs(goal) 

    n2 = len(sum2)
    for s1 in sum1:
        t = goal-s1 
        if t == 0: return 0

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

nums = [5, -7, 3, 5]
nums = [7,-9,15,-2]
nums = [1,2,3]
#ans = findAllSums(nums)
#print(ans)
goal = -7
ans = minAbsDifference1(nums, goal) 
print(ans)
        


    