# https://www.lintcode.com/en/old/problem/graph-valid-tree/
# https://leetcode.com/problems/graph-valid-tree/

def validTree1(n, edges, root):
    '''
    when root is known & want to start search from Top -> Bottom (ie alike directed Acyclic Graph)
    :param n: number of vertexes
    :param edges: list of directed (edges)
    :param root: vertex number of root
    '''
    if not n:
        return True 
    
    #1. Define Adjacency Matrix
    adj = {v:[] for v in range(n)}

    # We are treating as Directed Acyclic Graph = Tree
    for v1, v2 in edges:
        adj[v1].append(v2)

    print(adj)

    # TREE = Directed Acyclic Graph

    #2. define dfs
    visited = set()
    def dfs(v):
        if v in visited:
            #print(v)
            return True  # Cycle detected

        visited.add(v)

        for neig in adj[v]:
            if dfs(neig):
                return True

    isCycle = dfs(root)
    print(isCycle)
    print(visited)
    allNodesVisted = len(visited) == n
    print(allNodesVisted)
    isTree =(not isCycle) and allNodesVisted

    return isTree

def validTree2(n, edges):
    '''
    when root is unknown & need to start search from any random vertex (ie alike Undirected acyclic Graph)
    '''
    if not n:
        return True 
    
    #1. Define Adjacency Matrix

    adj = {v:[] for v in range(n)}

    # We are treating as Directed Acyclic Graph = Tree
    for v1, v2 in edges:
        adj[v1].append(v2)
        adj[v2].append(v1)

    # TREE = Directed Acyclic Graph

    #2. define dfs
    visited = set()
    def dfs(v, prev):
        '''
        :param v: vertex
        :param prev: prev vertex (ie connected to this vertex v)
        '''
        if v in visited:
            print(v)
            return False  # Cycle/Loop detected

        visited.add(v)

        for neig in adj[v]:
            if prev == neig: # Edge has already been explored earlier (False Positive)
                continue
            if not dfs(neig, v):
                return False
        
        return True

    noLoop = dfs(0, -1)
    allNodesVisted = len(visited) == n
    isTree = noLoop and allNodesVisted

    return isTree

n = 7
#edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2,6]]
print(validTree1(n, edges))

'''
Just because Edges are given randomly with label
& Edges are undirected we need to conside both the way in adjacency Matrix representation
Otherwise we will miss some vertexes

But If you are given root then you can consider Only 1 way of representation 
'''