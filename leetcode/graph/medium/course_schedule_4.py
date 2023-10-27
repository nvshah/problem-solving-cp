# https://leetcode.com/problems/course-schedule-iv/
from typing import List 
from collections import defaultdict

# O(N^3) 
def checkIfPrerequisite(numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    # Adjacency Matrix
    adj = defaultdict(list) # Direct Prerequisites map
    for a, b in prerequisites:
        adj[b].append(a) # [a] is prerquisite for [b]

    # All Preqrequisites (ie Direct + Indirect)
    preReqMap = {} # course -> {prequisites}
    
    def dfs(node):
        '''Find all the nodes that can reached via [node] including itself'''
        if node in preReqMap: return preReqMap[node]

        reachables = {node} # incuding itself
        for nei in adj[node]:
            reachables |= dfs(nei) # all nodes reachable via [nei]
        
        preReqMap[node] = reachables
        return reachables

    # Run DFS to populate all the prerequisites for all courses
    for course in range(numCourses):
        dfs(course) 
    
    # --- Now [preReqMap] has info about prerequisites of all courses

    return [u in preReqMap[v] for u, v in queries]