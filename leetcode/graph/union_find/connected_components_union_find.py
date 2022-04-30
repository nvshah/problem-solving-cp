# https://cheonhyangzhang.gitbooks.io/leetcode-solutions/content/323-number-of-connected-components-in-an-undirected-graph.html
from typing import List

'''
Que :- Find the number of Connected Components in Undirected Graph
 
 Given (Inputs) :- 
   1. {edges} :- list of Edge
   2. {n} :- number of nodes in graph
 Outputs :- #connected-components

 Similar Que (LeetCode) :- #547 -> numbers of Province

'''

def countComponents1(n: int, edges: List[List[int]]) -> int:
    '''
        Approach 1 Using Union & Find
    '''
    # initially all nodes are parent to themselves
    parents = [i for i in range(n)]  
    # rank[i] = number of nodes part of that group where {i} is the leader|parent
    ranks = [1]*n

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
    
    def union(v1, v2):
        '''
        v1 & v2 are 2 elements linked by edge
        :param v1: edge endpoint 1
        :param v2: edge endpoint 2

        Group the {v1}, {v2} into appropriate group
        return 1 if they have been included in either of group (ie New Group is composed)
               0 if they already belong to same appropriate group
        '''
        # root parents for both the elem {v1} & {v2}
        p1, p2 = find(v1), find(v2) 

        if p1 == p2:  # both of them already belong to same group
            return 0

        # new group need to be formed
        if ranks[p1] >= ranks[p2]:
            # group with root={p1} has more or equal members, so include all members from p2's group into it
            parents[p2] = p1
            ranks[p1] += ranks[p2]
        else:
            # group with root={p2} has more members, so include all members from p1's group into it
            parents[p1] = p2
            ranks[p2] += ranks[p1]
        
        return 1  # new group formed

    components = n # initially all elem are individual components
    for n1, n2 in edges:
        components -= union(n1, n2)

    return components


def countComponents2(n: int, edges: List[List[int]]) -> int:
    '''
        Approach 1 Using Union & Find
    '''
    # initially all nodes are parent to themselves
    parents = [i for i in range(n)]  
    # rank[i] = number of nodes part of that group where {i} is the leader|parent
    ranks = [1]*n  # ranks[i] will be non-zero if i is root else it will be 0

    def find(v):
        '''find the parent for this member {v} in the graph'''
        p = v   # every elem {m} has atleast parent itself in worst case

        # 1. find the root
        while p != parents[p]:
            p = parents[p]

        # 2. Path Compression for all members of P's grp
        while v != p: 
            parents[v], v = p, parents[v]
            
        
        # {p} is the root of group where {v} belongs
        return p
    
    def union(v1, v2):
        '''
        v1 & v2 are 2 elements linked by edge
        :param v1: edge endpoint 1
        :param v2: edge endpoint 2

        Group the {v1}, {v2} into appropriate group
        return 1 if they have been included in either of group (ie New Group is composed)
               0 if they already belong to same appropriate group
        '''
        # root parents for both the elem {v1} & {v2}
        p1, p2 = find(v1), find(v2) 

        if p1 == p2:  # both of them already belong to same group
            return 0

        # new group need to be formed
        if ranks[p1] >= ranks[p2]:
            # group with root={p1} has more or equal members, so include all members from p2's group into it
            parents[p2] = p1
            ranks[p1] += ranks[p2]  # add all members of {p2} -> {p1}
            ranks[p2] = 0  # update rank of {p2} as {p2} is no longer root
        else:
            # group with root={p2} has more members, so include all members from p1's group into it
            parents[p1] = p2
            ranks[p2] += ranks[p1] # add all members of {p1} -> {p2}
            ranks[p1] = 0  # update rank of {p1} as {p1} is no longer root
        
        return 1  # new group formed

    components = n # initially all elem are individual components
    for n1, n2 in edges:
        components -= union(n1, n2)

    return components


if __name__ == '__main__':
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]  # ans -> 2

    edges = [[0, 1], [1, 2], [2, 3], [3, 4]] # ans -> 1

    ans1 = countComponents1(n, edges)
    ans2 = countComponents2(n, edges)

    print(ans1, ans2)

    






