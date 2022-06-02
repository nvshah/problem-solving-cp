# https://leetcode.com/problems/network-delay-time/
from collections import defaultdict
import heapq
from typing import List

'''Concepts :- BFS | Heap | Set'''

def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for s, d, t in times:
        graph[s].append((t, d))  # t -> time, d -> dest 
        
    visit = set()
    hp = [(0, k)]   # heap of (time, destination)
    
    cnt = 0
    while hp:
        time, no = heapq.heappop(hp)
        
        if no in visit: continue
        visit.add(no)
        
        if len(visit) == n: return time  # visited all or not !
        
        # check neigbors
        for tm, nei in graph[no]:
            if nei not in visit:
                heapq.heappush(hp, (tm+time, nei))
    
    return -1