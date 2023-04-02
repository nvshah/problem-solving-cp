# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/
from typing import List
from collections import defaultdict

def minScore(n: int, roads: List[List[int]]) -> int:
    # 1. create neighbors info map
    adj = defaultdict(list)     # (to, distance)
    for src, end, dist in roads:
        adj[src].append((end, dist))
        adj[end].append((src, dist))

    res = float('inf')
    visited = set() 

    # NOTE: as nodes can be visited multiple times so we need to visit all nodes & all edges
    #  ie O(e+v) 

    # 2. DFS
    def dfs(node):
        if node in visited:
            # as all towards edges are already discovered
            return 

        visited.add(node)

        nonlocal res
        for nei, dist in adj[node]:
            res = min(res, dist)              
            dfs(nei)
        
    dfs(1)
    return res
        
        
        
    return res