# https://leetcode.com/problems/minimize-deviation-in-array/
from typing import List
from operator import itemgetter
import heapq

'''
Idea
1. Find lower limit for all the members that they can go to. 
   NOTE: here we do need to track original val (to get idea ie from its lowest limit it can
         come back to its original val)
2. then gradually try to shift & increase them to their respective upper limit | original value !
'''

def isOdd(num): return num & 1 

def minimumDeviation(nums: List[int]) -> int:
    res = float('inf')  # minimzed (maximal diff)

    # Keep track of all deviated candidate values := "current deviated array"
    minHeap = []  # (candidate_val, highest_cap)  // highest_cap is the val this deviated {candidate_val} can grow to.
    
    # max val present in current deviated array (ie minHeap)
    heapMax = 0

    # compute the lowest limit to which all the members of array can be deviated to :
    # & mark this lowest limit as starting candidate for deviated values (ie those would be member of minHeap)
    for n in nums:
        if isOdd(n):
            # for odd num n,
            #  lowest deviated val := n         // cur
            #  highest deviated val := n * 2    // upto
            # Eg 1 -> 2  // upto
            #    3 -> 6  // upto
            cur, upto = n, n*2
        else:
            # for even num n,
            #  lowest deviated val :
            cur = n
            while not isOdd(cur):
                cur //= 2  
            #  highest deviated val := n    // upto
            upto = n

        # add candidate 
        minHeap.append((cur, upto))
    
    # Find the max val among current deviated candidate vals 
    heapMax = max(minHeap, key=itemgetter(0))[0]

    # Heapify the candidates to get minimzed (max difference) as early as possible
    heapq.heapify(minHeap)

    # Try picking each candidate and progressing them to highest possible val
    #while len(minHeap) == size:
    while True:
        # once any candidate (ie deviated val) reach to its maxCap, we are done
        # As that would be the minimized (max difference) between 2 elem possible in deviated array
        cand, maxCap = heapq.heappop(minHeap)

        # compute the difference := MAIN CRITERIA
        diff = heapMax - cand  # maximal diff
        res = min(res, diff)   # minimized maximal diff tracking

        # If [cand] reach to its maxCap, then we found our ans
        if cand == maxCap:
            return res 

        # progress [cand] towards its maxCap
        newVal = cand * 2
        heapq.heappush(minHeap, (newVal, maxCap))
        # update curr max val in deviated Array as well 
        heapMax = max(heapMax, newVal)
        



