# https://leetcode.com/problems/longest-happy-string/

import heapq
from collections import Counter

'''
Idea :- Max Heap
'''

def longestDiverseString(a: int, b: int, c: int) -> str:
    ''' 
    Idea :- Pick the character with max count at first (ie in priority)
            To track char with max count we will use Heap or likewise DataStructure
    '''
    # 1. keep Track of all valuable characters
    chars = Counter(a=a, b=b, c=c)
    # 2. -ve Cnts as we need to create max-Heap so we require -ve of freq 
    #    item :- (-cnt, char)
    maxHeap = [(-itm[1], itm[0]) for itm in chars.items() if itm[1]]

    # a + b + c > 0 (GIVEN)

    # 3. create max heap (ie via Heapifying Inplace)
    heapq.heapify(maxHeap)

    res = []  # hold the accumulated characters

    # ! Note :- inorder to decrease the cnt we need to add 1
    #         Eg cnt = -4, new_cnt = -4+1 = -3 & 
    #            act_cnt = 3   //effective actual cnt ie ignoring -ve sign 
    def updateHeap(char, cnt):
        res.append(char) # update res by accounting this {char}
        # update the max-heap
        cnt += 1  # decrease the cnt of character effectively in Max-Heap
        if cnt:
            heapq.heappush(maxHeap, (cnt, char))

    # 4. try to consume as much char as it can
    while maxHeap:
        # get character with max freq at present
        cnt1, char1 = heapq.heappop(maxHeap)  # top-most character
        # check constraints of 'ccc'  // c := char
        if len(res) > 1 and char1 == res[-1] == res[-2]:
            if not maxHeap: break  # as no char left
            cnt2, char2 = heapq.heappop(maxHeap)  # second top-most character
            updateHeap(char2, cnt2)  # update res and heap (if so)
        if cnt1:
            updateHeap(char1, cnt1)  # update res and heap (if so)

    return ''.join(res)

a,b,c =1,1,7
ans = longestDiverseString(a,b,c)
print(ans)