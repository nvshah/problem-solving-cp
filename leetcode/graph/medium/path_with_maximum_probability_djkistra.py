# https://leetcode.com/problems/path-with-maximum-probability/
from typing import List
from collections import defaultdict
import heapq

'''
IDEA

Djkistra Algo,
where we will aim to find the path with nodes that leads to max probbaility instead 
of min-nodes (ie shortest path)
Thus instead of aiming for shortest path we will try to find that yields max-probability

NOTE: instead of Queue, we will use MaxHeap for candidates as traversal progress.
'''


def maxProbability(n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

    # 1. create adjancency map
    adj = defaultdict(list) # src -> [(dest, prob)]
    for (s, d), p in zip(edges, succProb):
        adj[s].append((d, p))
        adj[d].append((s, p))

    # 2. Dijkstra's Algo
    # NOTE: instead of Queue, we will use PriorityQueue (ie MaxHeap) for candidates as traversal progress. 

    # {pq} is a Max-Heap, which pick next reachable node with highest probability
    pq = [(-1, start)] # (probability, tobeVisitedNode)

    visited = set()  # keep track of visited node

    while pq:
        # 1. pick the candidate node 
        prob, node = heapq.heappop(pq)
        visited.add(node)

        # 2. check of completion
        if node == end:
            return -prob  # -ve as max-heap
        
        # 3. visit & mark neighbors as candidate
        for nei, nProb in adj[node]:
            if nei not in visited:
                # consider [nei] as a candidate
                heapq.heappush(pq, (prob * nProb, nei))  # -ve as maxHeap

    return 0      

            




