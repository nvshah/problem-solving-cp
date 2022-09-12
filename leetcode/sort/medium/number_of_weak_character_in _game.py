# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

from collections import defaultdict
from typing import List


# Idea 1 : Simple Sort
'''REFER THIS SOLN'''
def numberOfWeakCharacters(properties: List[List[int]]) -> int:

    # For character with same attacks, the one with max defesne would be candidate
    # As other in same group are negligible or should be shadowed by one with max defense attack
    properties.sort(key=lambda x: (-x[0], x[1]))  # sort attack wise

    maxDef = properties[0][1] # Max Defence till now
    cnt = 0

    for _, d in properties[1:]:
        if d < maxDef:
            cnt += 1
        else: 
            maxDef = max(d, maxDef)
    
    return cnt

def numberOfWeakCharacters2(properties):
    '''Bucket Sort O(n)'''
    bucket = defaultdict(list)
    for a, d in properties:
        bucket[a].append(d)
    
    s = min(bucket.keys())
    e = max(bucket.keys())

    maxDef = -1
    cnt = 0
    for i in range(e, s-1, -1):
        if i not in bucket: continue 
        cnt += len([d for d in  bucket[i] if d < maxDef])
        # for d in bucket[i]:
        #     if d < maxDef:
        #         cnt += 1

        maxDef = max(maxDef, d)
    return cnt


'''
As lenght of properties and max value of attack & defense are same in worst case
'''
def numberOfWeakCharacters3(properties: List[List[int]]) -> int:

    # For character with same attacks, the one with max defesne would be candidate
    # As other in same group are negligible or should be shadowed by one with max defense attack
    properties.sort(key=lambda x: (x[0], -x[1]))  # sort attack wise

    maxDef = properties[-1][1] # Max Defence till now
    cnt = 0

    for _, d in properties[-2::-1]:
        if d < maxDef:
            cnt += 1
        else: 
            maxDef = max(d, maxDef)
    
    return cnt


    



