# https://leetcode.com/problems/shortest-path-with-alternating-colors/
from typing import List
from collections import defaultdict, deque

# Multi-Src BFS (ie Parallel BFS)
'''
Idea -> start 2 parallel bfs for red & blue paths from 0
'''

def shortestAlternatingPaths1(n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    # create adjacency matrix 
    redAdj = defaultdict(list) 
    blueAdj = defaultdict(list)

    for src, dest in redEdges:
        redAdj[src].append(dest)

    for src, dest in blueEdges:
        blueAdj[src].append(dest)

    # Multi-Src BFS (ie 2 parallel BFS for Possible Blue & White Edges Path)
    paths = [-1] * n 

    # start from node -> 0

    # (node, length, prev_edge_color) -> 
    #  length: length of path from [0] to reach [node]
    #  viaEdge: color of edge used to reach [node], recently
    que = deque([(0, 0, None)]) # (node, length, viaEdge)
    visited = {(0, None)} #(node, viaEdge) // [node] visited via [viaEdge] edge-color
    
    while que: 
        node, distance, prevEdgeColor = que.popleft()

        if paths[node] == -1: # visited for first time 
            # & hence found shortest path for [node] from 0
            paths[node] = distance 

        if prevEdgeColor != 'RED':
            # Alternating
            for nei in redAdj[node]:
                if (nei, 'RED') not in visited:
                    # visit [nei] via edge having [color]
                    visited.add((nei, 'RED'))
                    que.append((nei, distance+1, 'RED'))
        
        if prevEdgeColor != 'BLUE':
            # Alternating
            for nei in blueAdj[node]:
                if (nei, 'BLUE') not in visited:
                    # visit [nei] via edge having [color]
                    visited.add((nei, 'BLUE'))
                    que.append((nei, distance+1, 'BLUE'))

    return paths

# Slightly Modified - A2
def shortestAlternatingPaths(n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    # create adjacency matrix 
    redAdj = defaultdict(list) 
    blueAdj = defaultdict(list)

    for src, dest in redEdges:
        redAdj[src].append(dest)

    for src, dest in blueEdges:
        blueAdj[src].append(dest)

    # Multi-Src BFS (ie 2 parallel BFS for Possible Blue & White Edges Path)
    paths = [-1] * n 

    # start from node -> 0

    # (node, length, prev_edge_color) -> 
    #  length: length of path from [0] to reach [node]
    #  viaEdge: color of edge used to reach [node], recently
    que = deque([(0, 0, None)]) # (node, length, viaEdge)
    visited = {(0, None)} #(node, viaEdge) // [node] visited via [viaEdge] edge-color
    
    while que: 
        node, distance, prevEdgeColor = que.popleft()

        if paths[node] == -1: # visited for first time 
            # & hence found shortest path for [node] from 0
            paths[node] = distance 

        sources = [('RED', redAdj), ('BLUE', blueAdj)]

        for color, adj in sources:
            if prevEdgeColor != color:
                # Alternating
                for nei in adj[node]:
                    if (nei, color) not in visited:
                        # visit [nei] via edge having [color]
                        visited.add((nei, color))
                        que.append((nei, distance+1, color))

    return paths 


 
