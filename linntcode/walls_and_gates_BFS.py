# https://www.lintcode.com/problem/walls-and-gates/description
# https://leetcode.com/problems/walls-and-gates/

from collections import deque

def wallsAndGates(rooms):
    ''' BFS Traversal From Each Gate Simulataneously to explore each room which is nearby 
        Simulataneous Gate explore
    '''
    rows, cols = len(rooms), len(rooms[0])
    visit = set()  # keep track of empty rooms which are visited already (in BFS )
    q = deque()    # Keep track of next nearest room at each stage

    def addRoom(r, c):
        if (0 <= r < rows) and (0 <= c < cols): # isBounded
            isNotWall = rooms[r][c] != -1  # obstacle
            isNotVisited = (r,c) not in visit
            if isNotVisited and isNotWall:
                q.append((r,c))
                visit.add((r,c))

    # Idea :- Visit nearest rooms from current Queue & start from Gate itself

    # Find the gates
    for i in range(rows):
        for j in range(cols):
            if rooms[i][j] == 0:  # gate
                addRoom(i, j)  # Add gate to Queue
    
    # dist is used whilst processing the nodes
    dist = 0 # distance of gate from gate is 0 so at level 1 -> dist of all room = 0
    neigh = [(0,1), (1,0), (0,-1), (-1,0)]
    while q:
        for _ in range(len(q)):
            # 1. Process & remove Room from Queue (Update the Distance of Room from gate)
            i, j = q.popleft()
            rooms[i][j] = dist  # dist at current level from gate 

            # 2. Add neighbors to Queue
            for nx, ny in neigh:
                addRoom(i+nx, j+ny)
        
        # Next level  (Pre-Prep of Distance from Gate -> Rooms) !
        # 3. Update Distance for all rooms at next level So (this dist can be used whilst processing those rooms)
        dist += 1

    return rooms
        