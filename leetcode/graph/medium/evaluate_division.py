# https://leetcode.com/problems/evaluate-division/
from typing import List
from collections import defaultdict

def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    g = defaultdict(list)  # list of (dest, cost)
    l = len(equations)
    
    # 1. build graph (Directed)
    for i in range(l):
        s, d = equations[i]  # num, denom
        v = values[i]
        g[s].append((d, v))   
        g[d].append((s, 1/v))
        
    # 2. Define DFS for graph traversal
    def dfs(s, d, visit):
        if (s not in g) or (d not in g): # cannot find destination
            return -1
        
        if s == d:   # Reach the Destination
            return 1
        
        visit.add(s)
        
        # search ahead path towards {d}
        for neigh, cost in g[s]:
            if neigh not in visit:
                r = dfs(neigh, d, visit)
                if r != -1:  # means reach the destination atleast
                    return r * cost
        return -1
    
    # 3 Evaluate queries
    res = [dfs(n, d, set()) for n, d in queries]
    
    return res