# https://leetcode.com/problems/delete-and-earn/
from os import uname
from typing import List
from collections import Counter
import operator as op


'''
Problem:
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

Idea :
1D DP

'''

def deleteAndEarn1(nums: List[int]) -> int:

    # 1. compute the freq of each num
    counts = Counter(nums)

    # 2. map s.t. (num -> total val after considering it frequency)
    score = {n:n*c for n,c in counts.items()}

    # dp - (need to track) last 2 val only
    #    e1 :- earn 1 : prev-to-prev computation(cached) (ie max earn till e1)
    #    e2 :- earn 2 : prev computation(cached)  (ie max earn till e2)
    e1, e2 = 0

    # 3. get sorted unique nums in increasing order so that 
    #    we can spot prev & next neighbor val easily 
    uNums = sorted(score.keys())
    l = len(uNums)
    
    if l == 1:
        return score[uNums[0]]

    for i, n in enumerate(uNums): # n := curr val
        currEarn = score[n]  # if considered the current num {n}

        # check for prev neighbor  // prev := uNums[i-1]  
        if i > 0 and uNums[i-1] + 1 != n:
            # we can use curr {n} & {prev} as they are not adjacent values
            newEarn = currEarn + e2
        else:
            # we can't use curr {n} & {prev} as they are adjacent values
            newEarn = max(currEarn + e1, e2)
        
        e1, e2 = e2, newEarn  # shift 2 pointer 1 step ahead
    
    return e2

def deleteAndEarn2(nums: List[int]) -> int:

    def getUpdatedPtrs(curr, prev, e1, e2):
        ''' get updated e1 & e2
            curr :- curr number
            prev :- prev number
            e1 :- last to last best earn
            e2 :- last cached best earn
        '''
        currEarn = score[curr]  # if considered the current num {n}
        if prev + 1 != curr:
            # we can use curr {n} & {prev} as they are not adjacent values
            newEarn = currEarn + e2
        else:
            # we can't use curr {n} & {prev} as they are adjacent values
            newEarn = max(currEarn + e1, e2)
        
        return e2, newEarn  # shift 2 pointer 1 step ahead

    # 1. compute the freq of each num
    counts = Counter(nums)

    # 2. map s.t. (num -> total val after considering it frequency)
    score = {n:n*c for n,c in counts.items()}

    # 3. get sorted unique nums in increasing order so that 
    #    we can spot prev & next neighbor val easily 
    uNums = sorted(score.keys())
    l = len(uNums)
    
    if l == 1:
        return score[uNums[0]]

    
    # dp - (need to track) last 2 val only
    #    e1 :- earn 1 : prev-to-prev computation(cached) (ie max earn till e1)
    #    e2 :- earn 2 : prev computation(cached)  (ie max earn till e2)

    # Edge case i=0
    e1, e2 = getUpdatedPtrs(uNums[0], -1, 0, 0)

    # 4. make move e2 -> till end
    for i in range(1, len(uNums)): 
        e1, e2 = getUpdatedPtrs(uNums[i] , uNums[i-1], e1, e2)
    
    return e2

def deleteAndEarn3(nums: List[int]) -> int:

    def getUpdatedPtrs(curr, prev, e1, e2):
        ''' get updated e1 & e2
            curr :- curr number
            prev :- prev number
            e1 :- last to last best earn
            e2 :- last cached best earn
        '''
        currEarn = curr*counts[curr]  # if considered the current num {n}
        if prev + 1 != curr:
            # we can use curr {n} & {prev} as they are not adjacent values
            newEarn = currEarn + e2
        else:
            # we can't use curr {n} & {prev} as they are adjacent values
            newEarn = max(currEarn + e1, e2)
        
        return e2, newEarn  # shift 2 pointer 1 step ahead

    # 1. compute the freq of each num
    counts = Counter(nums)

    # 3. get sorted unique nums in increasing order so that 
    #    we can spot prev & next neighbor val easily 
    uNums = sorted(counts.keys())
    l = len(uNums)
    
    if l == 1:
        v = uNums[0]
        return v * counts[v]
    
    # dp - (need to track) last 2 val only
    #    e1 :- earn 1 : prev-to-prev computation(cached) (ie max earn till e1)
    #    e2 :- earn 2 : prev computation(cached)  (ie max earn till e2)

    # Edge case i=0
    e1, e2 = getUpdatedPtrs(uNums[0], -1, 0, 0)

    # 4. make move e2 -> till end
    for i in range(1, len(uNums)): 
        e1, e2 = getUpdatedPtrs(uNums[i] , uNums[i-1], e1, e2)
    
    return e2



if __name__ == '__main__':
    nums = [3,4,2]
    ans = deleteAndEarn2(nums)

    print(ans)