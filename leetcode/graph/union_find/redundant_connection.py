# https://leetcode.com/problems/redundant-connection/
from typing import List

'''
Union-Find
'''


def findRedundantConnection(edges: List[List[int]]) -> List[int]:
    n = len(edges)  # number of nodes
    # initially all nodes are parent to themselves
    # NOTE : 0th index will be useless as node starts from 1 -> n (so taking n+1 instead of n below)
    parents = [i for i in range(n+1)]  
    # rank[i] = number of nodes part of that group where {i} is the leader|parent
    ranks = [1]*(n+1)

    def find(m):
        '''find the parent for this member {m} in the graph'''
        p = m   # every elem {m} has atleast parent itself in worst case

        # root node := when node's parent is node itself
        while p != parents[p]:
            p = parents[p] # move 1 step closer to root of the group
            # Path Compression | Optimization :- (Point current elem {m} to its GrandParent instead of parent)
            parents[p] = parents[parents[p]]
        
        # {p} now points to root elem of the group in which {m} is one of the member
        return p
    
    def union(n1, n2):
        '''
        Link the elemennt into same group if they aren not already
        return True if linked together 
               False if already beling to same group
        '''
        # root parents for both the elem {v1} & {v2}
        p1, p2 = find(n1), find(n2) 

        if p1 == p2:  # both of them already belong to same group
            return False

        # new group need to be formed
        if ranks[p1] >= ranks[p2]:
            # group with root={p1} has more or equal members, so include all members from p2's group into it
            parents[p2] = p1
            ranks[p1] += ranks[p2]
        else:
            # group with root={p2} has more members, so include all members from p1's group into it
            parents[p1] = p2
            ranks[p2] += ranks[p1]
        
        return True  # new group formed

    for n1, n2 in edges:
        if not union(n1, n2):
            # as both of them belong to same group so adding edge betweeen them create a cycle in that group
            return [n1, n2]  