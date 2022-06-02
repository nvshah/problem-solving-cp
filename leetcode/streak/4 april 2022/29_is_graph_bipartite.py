from typing import List 

'''Gaph Coloring technique'''

'''Via DFS'''
def a1(graph: List[List[int]]):
    n = len(graph) # nodes cnt
    # color mapping :
    # 0 :- not allocated, 1 :- Grp1(Red), -1 : Grp2(Blue)
    colors = [0]*n
    
    def isValid(i, c):
        '''
        DFS
        check if color to given node {i} is valid for Bipartite Graph
        (allocate if required)
        i := node
        c := color that needs to be allocated to {i}
        '''
        given = c
        if colors[i] == 0:
            # Provide color
            colors[i] = c
            
            # check for neighbors
            adj = graph[i]
            for nei in adj:
                if not isValid(nei, -given):
                    return False
        else:
            # Validate color
            given = colors[i]
            if given != c:  # contradict
                return False
            
        return True
    
    for i in range(n):
        if colors[i]==0:
            if not isValid(i, 1):
                return False
    return True

''' Via BFS'''
def a2(graph):
    n = len(graph) # nodes cnt
    # color mapping :
    # 0 :- not allocated, 1 :- Grp1(Red), -1 : Grp2(Blue)
    colors = [0]*n
    
    for i in range(n):
        if colors[i]==0:
            # 1. assign code
            colors[i] = 1
            # 2. check for neighbors via bfS
            q = [(i, 1)]  # queue|list -> (idx, color) // As here order doesn't matter to travel children
            while q:
                idx, color = q.pop()
                neigh = graph[idx]
                for nei in neigh:
                    if colors[nei] == color: # conflict
                        return False
                    elif colors[nei] == 0: # new node & hence not assigned code|color
                        colors[nei] = -color
                        q.append((nei, -color))
    return True
                    

''' Via Union & Find '''
def a3(graph):
    '''Idea :- Any 2 nodes in same group (after union) must not have edge between them'''
    n = len(graph) # nodes cnt
    parents = [i for i in range(n)] # initially all nodes are parent to itself
    
    def union(x, y):
        px = find(x)
        py = find(y)
        
        if px != py:
            parents[py] = px  # merge 2 diff grp
    
    '''Find the parent for {n}'''
    def find(n):
        t = n
        # find the root parent for {n}
        while parents[t] != t:
            t = parents[t]
        
        root = t
        
        cur = n
        # path compression
        while cur != t:
            parents[cur], cur = root, parents[cur]
        
        return root
        
    # NOTE :- In same group no 2 members should have edge between them
    for i in range(n):
        child = graph[i]  # child of {i}
        if not child: continue
        head = child[0]  # Let first node in grp to represent parent
        
        # Thus {i} & its {child} must be in seperate grp
        for c in child:
            # check if {c} & {i} have diff parents
            if parents[c] == parents[i]: return False
            # Do include {c} in 1 grp ie opposite to grp of {i}
            union(c, head)
        
    return True
                        
                    
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #return a1(graph)
        #return a2(graph)
        return a3(graph)