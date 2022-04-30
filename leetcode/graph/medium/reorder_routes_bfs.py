# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
from collections import defaultdict
from typing import List

'''
Assumptions :

- There is no loop in the graph
- Graph is Connected
'''

# Third Priority
def minReorder1(n: int, connections: List[List[int]]) -> int:
    edges = {(a,b) for a,b in connections} # route from city a -> b
    neighbors = defaultdict(list) # adjacency Map for city -> [neighbors]  // ignoring route direction
    visited = set() # keep track of visited nodes

    for a, b in connections:
        # Note here route direction is ignored & just connected or not is checked !
        neighbors[a].append(b)
        neighbors[b].append(a)

    def dfs(city, changes):
        '''
        -> Explore each city & find total route chanes needed in dfs manner 
        -> recursively check the neighbors

        :param city :- curr city
        :param changes :- total changes happened till now (ie count outgoing edges)
        '''
        print(city, changes, '-----')
        # as graph is connected so its ensure that city has atleast neighbors
        for ncity in neighbors[city]:
            print(f'{visited=}', 'nCity', ncity)
            if ncity in visited:
                continue
            # 1. check if route is not in inward direction
            if (ncity, city) not in edges:
                changes += 1
            # 2. check further neighbors
            visited.add(ncity)
            changes = dfs(ncity, changes)
        
        return changes
        
    # Mark current city as well
    visited.add(0)  # city -> 0  // starting point
    return dfs(0, 0)

# First Priority
def minReorder3(n: int, connections: List[List[int]]) -> int:
    edges = {(a,b) for a,b in connections} # route from city a -> b
    neighbors = defaultdict(list) # adjacency Map for city -> [neighbors]  // ignoring route direction
    visited = set() # keep track of visited nodes

    for a, b in connections:
        # Note here route direction is ignored & just connected or not is checked !
        neighbors[a].append(b)
        neighbors[b].append(a)
    
    changes = 0

    def dfs(e1, e2):
        '''
        -> Explore each city & find total route chanes needed in dfs manner 
        -> recursively check the neighbors

        :param e1 :- start city 
        :param e2 :- target(end) city
        '''
        nonlocal changes

        if e1 in visited: return 

        # 1. check if route direction needs alteration | Visit city {e1}
        if (e1, e2) not in edges:
            changes += 1

        # 2. visited the city {e1}
        visited.add(e1)

        # 3. visit neighbors of city {e1}
        #    NOTE : as graph is connected so its ensure that city has atleast neighbors
        for n in neighbors[e1]:
            dfs(n, e1)

    dfs(0, -1) # dummy node {-1} to start node {0}
    return changes-1  # -1 for edge by dummy node {-1}

# Second Priority
def minReorder2(n: int, connections: List[List[int]]) -> int:
    edges = {(a,b) for a,b in connections} # route from city a -> b
    neighbors = defaultdict(list) # adjacency Map for city -> [neighbors]  // ignoring route direction
    visited = set() # keep track of visited nodes

    for a, b in connections:
        # Note here route direction is ignored & just connected or not is checked !
        neighbors[a].append(b)
        neighbors[b].append(a)

    changed = 0
    def dfs(city):
        '''
        -> Explore each city & find total route chanes needed in dfs manner 
        -> recursively check the neighbors

        :param city :- curr city
        :param changes :- total changes happened till now (ie count outgoing edges)
        '''
        nonlocal changed 
        # as graph is connected so its ensure that city has atleast neighbors
        for ncity in neighbors[city]:
            print(f'{visited=}', 'nCity', ncity)
            if ncity in visited:
                continue
            # 1. check if route is not in inward direction
            if (ncity, city) not in edges:
                changed += 1
            # 2. check further neighbors
            visited.add(ncity)
            dfs(ncity)
        
    # Mark the starting city as visited
    visited.add(0)
    dfs(0)  # city -> 0 // starting point
    return changed



n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]

n = 5
connections = [[1,0],[1,2],[3,2],[3,4]]
ans = minReorder3(n, connections)
print(ans)