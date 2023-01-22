# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
from typing import List


def minTime(n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
    adj = {i:[] for i in range(n)}

    # As graph is not directed so we need Bi-Directional relation (going up & down)
    for l, r in edges:
        adj[l].append(r)
        adj[r].append(l)
    
    # As in Tree Data Structure the only way of stucking in cycle is going back via parent up
    # because Tree is Acyclic Graph 
    # (So there is no other way then goging via parent to produce the cycle in graph (ie BiDirectional Tree)
    def dfs(curr, parent):
        time = 0  # To collect apple from curr node time = 0

        for child in adj[curr]:
            if child == parent: continue # As this is going back (so will lead to loop/cycle)

            childTime = dfs(child, curr) # Time to collect all apples considering {child} as root node
            if childTime != 0 or hasApple[child]:
                # We need to step down to [child] level 
                # As Either [child] or its children has apples
                time += 2 + childTime  # 2 for moving to [child] level (1 step down)
        
        return time

    return dfs(0, -1)  # -1 as 0 itself is Root
    