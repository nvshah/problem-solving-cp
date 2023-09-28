# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/
from typing import List
from collections import defaultdict, deque


def closestMeetingNode(edges: List[int], node1: int, node2: int) -> int:
    '''
    1. Compute adjacency list (ie node reachability) of given graph
    2. find distance for common reachable nodes for node1 & node2 (via dfs or bfs), individually
    3. find nearest among discovery in step-2
    '''
    n = len(edges) # each node has at most one outgoing edge. hence 2 nodes -> 2 edges

    adj = defaultdict(list)
    for s, d in enumerate(edges):
        adj[s].append(d)

    # 2. build distance map for each reachable nodes from node1
    def bfs(node, distMap):
        '''find and fill the distMap for [node] as a source
        # hence distMap serve as 2 purpose (to check if node is visited & to track distance for each reachable node)
        '''
        que = deque([(node, 0)]) # Queue :- (dest, dist)
        distMap[node] = 0
        while que:
            dest, dist = que.popleft()
            for nei in adj[dest]:
                if nei not in distMap:  # to avoid circular-looping
                    que.append((nei, dist + 1))
                    distMap[nei] = dist+1
            
    # node -> distance from node
    distMap1 = {}
    distMap2 = {}
    bfs(node1, distMap1)
    bfs(node2, distMap2)
    common_reachable_nodes = distMap1.keys() & distMap2.keys() - {-1}
    print(common_reachable_nodes)
    if common_reachable_nodes:
        INF = float('inf')
        return min(range(n), key = lambda x: max(distMap1[x], distMap2[x]) if x in common_reachable_nodes else INF)
    return -1

edges = [4,4,8,-1,9,8,4,4,1,1]

edges = [-1,33,94,39,31,54,24,16,43,-1,79,60,72,-1,40,76,47,86,71,47,55,-1,-1,60,-1,77,-1,-1,89,-1,-1,9,35,-1,-1,88,-1,83,-1,33,17,68,22,71,-1,-1,-1,45,-1,-1,92,60,-1,-1,2,11,33,68,-1,61,94,-1,18,16,97,63,6,89,64,56,77,16,21,-1,71,36,46,-1,36,53,-1,-1,25,96,65,48,23,49,-1,-1,-1,32,-1,89,64,-1,46,-1]

ans = closestMeetingNode(edges, 5, 6)
print(ans)

                

