# https://leetcode.com/problems/russian-doll-envelopes/
from typing import List
from bisect import bisect_left

'''Return the length of longest incr subseq'''
def lisLen(seq):
    sz = len(seq)
    # LIS[i] denotes the maximum Length Of Subseq possible for characters from index {i} if i included
    LIS = [1]*sz  # LIS

    for i in range(sz-2, -1, -1):
        # we can take one by one combination with sub-indexes
        for j in range(i+1, sz):
            if seq[i] < seq[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])
            
    return max(LIS)

'''Naive :- Still its not a good approach'''
def maxEnvelopes1(envelopes: List[List[int]]) -> int:
    # 1. sort according to width in (w, h) 
    #    on Tie := Give pref to Bigger Envelope First (inorder to prevent from involving multiple same width envelope)
    envelopes.sort(key= lambda x: (x[0], -x[1]))

    # Now width are already sorted so need to find 
    # the Longest Incr SubSeq Height-Wise
    heights = [e[1] for e in envelopes]

    res = lisLen(heights)
    return res

''' Binary Search | Insertion Sort | LIS | DP '''
def maxEnvelopes2(envelopes: List[List[int]]) -> int:
    # 1. sort according to width in (w, h) 
    #    on Tie := Give pref to Bigger Envelope First (inorder to prevent from involving multiple same width envelope)
    envelopes.sort(key= lambda x: (x[0], -x[1]))

    # LIS := hold the best increasing heights  (at moment)
    dp = []  # it will consist of unique elems only (in icreasing order)

    # in this dp, new num will try to take seat in exisiting fashion 
    # (if not possible then new seat will ne allocated)

    for w, h in envelopes:
        #print(dp)
        i = bisect_left(dp, h)
        if i == len(dp):
            dp.append(h) # add at end of sorted dp
        else:
            dp[i] = h  # add {h} to correct pos {i}
    
    return len(dp)

envelopes = [[5,4],[6,4],[6,7],[2,3]]
envelopes = [[1,1],[1,1],[1,1]]
ans = maxEnvelopes2(envelopes)
print(ans)