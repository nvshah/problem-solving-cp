# https://leetcode.com/problems/diagonal-traverse-ii
from typing import List
from collections import defaultdict, deque
from itertools import chain

def findDiagonalOrder2(nums: List[List[int]]) -> List[int]:
    '''BFS | Queue '''
    res = []
    N = len(nums)
    que = deque([(0,0)]) # (i, j)

    while que:
        i, j = que.popleft()
        res.append(nums[i][j])

        if j == 0 and i != N-1:  # first col & not last Row
            que.append((i+1, j)) # below cell

        if j+1 < len(nums[i]):   # more elem on right
            que.append((i, j+1)) # right cell
    
    return res 

def findDiagonalOrder(nums: List[List[int]]) -> List[int]:
    '''Diagonal Key | Map'''
    diagMap = defaultdict(list) # diagId -> [elems]
    lastId = 0 # corresponds to last elem of longest Row

    # start from bottom to top
    for i in range(len(nums)-1, -1, -1):
        row = nums[i]
        for j in range(len(row)):
            diagMap[i+j].append(nums[i][j])
        lastId = max(lastId, i+j)  # as j is pointing to last idx of cur-row

    # ordered = map(diagMap.__getitem__, range(lastId+1))
    # return list(chain.from_iterable(ordered))
    
    res = []
    for i in range(lastId+1):
        res.extend(diagMap[i])

    return res  


    

#nums = [[1,2,3],[4,5,6],[7,8,9]]
nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
ans = findDiagonalOrder2(nums)
print(ans)