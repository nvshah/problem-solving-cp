# https://leetcode.com/problems/number-of-longest-increasing-subsequence/

from functools import partial
from typing import List
import itertools as it
import operator as op
from collections import defaultdict


def findNumberOfLIS(nums: List[int]) -> int:
    '''
     Idea :- DP on same array from Right to left
             As Comparing String of lenght 2 will include the Comparing String of length 1
    '''
    size = len(nums)
    # dp[i] denotes the maximum Length Of Subseq possible for characters from index {i} if i included
    LIS = [1]*size  # dP
    LIS_CNTS = [1]*size

    LIS_CNTS_M = defaultdict(int)

    for i in range(size-2, -1, -1):

        # we can take one by one combination with sub-indexes
        for j in range(i+1, size):
            if nums[i] < nums[j]:
                old = LIS[i]
                new = LIS[j] + 1
                if old == new: # more than 1 possibility for longest increasing subseq as of now
                    LIS_CNTS[i] += LIS_CNTS[j]
                elif old < new:
                    LIS_CNTS[i] = LIS_CNTS[j]
                LIS[i] = max(old, new)
    
    print(LIS)
    print(LIS_CNTS)
            
    m = max(LIS)

    print(LIS_CNTS_M)
    #return LIS_CNTS_M[m]
    
    return sum(it.compress(LIS_CNTS, map(op.eq, LIS, it.repeat(m))))

def findNumberOfLIS2(nums: List[int]) -> int:
    '''
     Idea :- DP on same array from Right to left
             As Comparing String of lenght 2 will include the Comparing String of length 1
    '''
    size = len(nums)
    # dp[i] denotes the maximum Length Of Subseq possible for characters from index {i} if i included
    lenLis, cntLis = 0, 0
    dp = {}  # len -> cnt

    for i in range(size-1, -1, -1):
        maxLen, maxCnt = 1, 1

        for j in range(i+1, size):
            if nums[i] < nums[j]:
                prevLen, prevCnt = dp[j]
                newLen = 1 + prevLen
                if newLen > maxLen:
                    maxLen = newLen
                    maxCnt = prevCnt
                elif newLen == maxLen:
                    maxCnt += prevCnt
        
        dp[i] = (maxLen, maxCnt)

        if maxLen > lenLis:
            lenLis, cntLis = maxLen, maxCnt
        elif maxLen == lenLis:
            cntLis += maxCnt

    return cntLis 

def findNumberOfLIS3(nums: List[int]) -> int:
    '''
     Idea :- DP on same array from Right to left
             As Comparing String of lenght 2 will include the Comparing String of length 1
    '''
    size = len(nums)
    # dp[i] denotes the maximum Length Of Subseq possible for characters from index {i} if i included
    dpLen = [1]*size  # dP for LIS-Len
    dpCnt = [1]*size  # dp for LIS-cnt
    lenCnt = defaultdict(int) # mapping ie len -> cnt

    for i in range(size-1, -1, -1):
        # we can take one by one combination with sub-indexes
        for j in range(i+1, size):
            if nums[i] < nums[j]:
                curr, prev = dpLen[i], dpLen[j]
                new = prev + 1
                if curr == new: # more than 1 possibility for longest increasing subseq as of now
                    dpCnt[i] += dpCnt[j]
                elif curr < new:
                    dpCnt[i] = dpCnt[j]

                dpLen[i] = max(curr, new)  # update the len for LIS
        
        lenCnt[dpLen[i]] += dpCnt[i]
    
    print(dpLen)
    print(dpCnt)
    print(lenCnt)
            
    m = lenCnt.popitem()    
    return m[1]

def findNumberOfLIS4(nums: List[int]) -> int:
    '''
     Idea :- DP on same array from Right to left
             As Comparing String of lenght 2 will include the Comparing String of length 1
    '''
    size = len(nums)
    # dp[i] denotes the maximum Length Of Subseq possible for characters from index {i} if i included
    len_lis = [1]*size  # dP
    cnt_lis = [1]*size

    for i in range(size-2, -1, -1):

        # we can take one by one combination with sub-indexes
        for j in range(i+1, size):
            if nums[i] < nums[j]:
                # 1. UPDATE COUNT
                old = len_lis[i]
                new = len_lis[j] + 1
                if old == new: # more than 1 possibility for longest increasing subseq as of now
                    cnt_lis[i] += cnt_lis[j]
                elif old < new:
                    cnt_lis[i] = cnt_lis[j]
                
                # 2. UPDATE LENGTH
                len_lis[i] = max(old, new)
    
    m = max(len_lis)  # max length of LIS
    # mop = partial(op.eq, m)
    # return sum(it.compress(cnt_lis, map(mop, len_lis)))
    
    return sum(cnt_lis[i] for i in range(size) if len_lis[i] == m)

    

#n = [1,3,5,4,7]
#n = [2,2,2,2,2]
#n = [1,3,2]
n = [1,2,4,3,5,4,7,2]
#n = [2,2,2,2,2]
a = findNumberOfLIS4(n)
print(a)