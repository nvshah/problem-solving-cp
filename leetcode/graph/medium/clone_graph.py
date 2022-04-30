# https://leetcode.com/problems/clone-graph/


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: Node) -> Node:
    oldToNew = {}  # keep track of new cloned node for corresp old node

    def clone(n):
        ''' 
        :param n: node
            Do clone the Graph via Recursive Cloning using DFS 
            Return the new clone node of {n} after all connection to neighbor is setup
        '''
        if n in oldToNew:
            return oldToNew[n]  # as this {n} already cloned so return that one from cache {oldToNew}

        
        # 1. Create clone for this {n}
        copy = Node(n.val)
        # 2. Cache the cloned {n}
        oldToNew[n] = copy 
        # 3. Connect neighbor's cloned for this {copy}
        copy.neighbors.extend([clone(adj) for adj in n.neighbors])
        
        return copy # clone

    return clone(node) if node else None
    