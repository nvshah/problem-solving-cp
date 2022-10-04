# https://leetcode.com/problems/the-skyline-problem/
import heapq
from typing import List

class Solution:

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        maxHeap = []
        ans = []  # skyline

        def updateSkyline(x):
            y = 0 if not maxHeap else maxHeap[0]
            ans.append([x, y])

        i = 0
        while i < len(buildings):
        #for l, r, h in buildings:
            l, r, h = buildings[i]
            # Remove all Stale or passed Left Side Buildings
            while maxHeap and maxHeap[0][2] < l:
                # Remove all buildings whose right point is hidden by current tall one
                tall_right = maxHeap[0][2]
                while maxHeap and maxHeap[0][2] <= tall_right:
                    heapq.heappop(maxHeap) 
                
                # Update the ans, Skyline point for [tall_right]
                updateSkyline(tall_right)
            
            heapq.heappush(maxHeap, (-h, l, r))
            i += 1
            # Consider all building starting at same point
            while i < len(buildings) and buildings[i][0] == l:
                nl, nr, nh = buildings[i]
                heapq.heappush(maxHeap, (-nh, nl, nr))
        
        while 


        