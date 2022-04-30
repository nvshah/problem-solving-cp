# https://leetcode.com/problems/min-cost-to-connect-all-points/
from typing import List
import heapq as hq


def minCostConnectPoints(points: List[List[int]]) -> int:
    '''
        Prim's Algo  (O (n^2 * log(n)) )
         O(n^2) -> for single pt -> visit rest pt (ie n-1) at each level So for n pts it will be n*(n-1) = O(n^2)
         O(log(n)) -> each time to pop elem from heap -> O(logn)
    '''

    n = len(points) # total points

    # * Each point is represented by its index
    # 1. Define the Adjancency List
    adj = {i:[] for i in range(n)} # i : list of [cost, point]  // point := idx 

    # ! NOTE : here the Graph is Undirected
    # 2. Fill the adjacency list (via manhatten dist)
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i+1, n):
            x2, y2 = points[j]
            dist = abs(x2-x1) + abs(y2-y1)
            # undirected graph so update cost bidirectionally
            adj[i].append((dist, j))
            adj[j].append((dist, i))
    
    # 3. Prim's
    res = 0 # min cost

    visited = set() # keep track of visited pts inorder to avoid cycles
    frontier = [(0,0)]  # Min heap that will hold list of (cost, point)  // point := idx

    # 3.1 BFS (using set + heap)
    while len(visited) != n:  # till all points are not visisted (ie connected)
        # 3.1.1 take min cost at moment
        cost, pt = hq.heappop(frontier)
        if pt in visited:
            continue 
        
        # 3.1.2 account this node & its corresp cost
        visited.add(pt)
        res += cost 

        # 3.1.3 BFS -> explore further (ie its neighbors)
        for nei in adj[pt]:
            if nei[1] not in visited:
                hq.heappush(frontier, nei)
    
    return res

