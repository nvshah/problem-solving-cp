# https://github.com/perron2/lean-file-picker/pull/4
from typing import List
from collections import defaultdict

class UnionFind:

    def __init__(self, n) -> None:
        self.par = list(range(n))
        self.rank = [0]*n

    def find(self, i):
        while i != self.par[i]:
            self.par[i] = self.par[self.par[i]]
            i = self.par[i]
        return i

    def unify(self, a, b):
        parA = self.find(a)
        parB = self.find(b)

        if parA == parB:
            return False
        
        if self.rank[parA] < self.rank[parB]:
            self.par[self.parA] = parB 
            self.rank[parB] += self.rank[parA]
        else:
            self.par[self.parB] = parA 
            self.rank[parA] += self.rank[parB]
        return True

class Solution:

    def numberOfGoodPaths(vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals) # number of nodes

        # Create the Adjacency Mapping for each node
        adj = defaultdict(list)
        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)

        # Create the grouping of vals:
        valIdxMap = defaultdict(list)
        for i, v in enumerate(vals):
            valIdxMap[v].append(i)

        res = 0
        uf = UnionFind(n)
        
        # Iterate vals in sorted order
        # So that we make ensure that all lower vals are already connected if any
        # Thus for any val k we will have already computed disjoint sets that has vals l.t k
        for v in sorted(valIdxMap):
            idxs = valIdxMap[v]
            # all the nodes in tree where val=v exists
            for i in idxs:
                # Find neighbors (that has smaller val) of such nodes & unify them with {i}
                for j in adj[i]:
                    if vals[j] <= v:
                        uf.unify(i, j) # j -> neighbor
            
            # All disjoints sets are created (regarding val v)
            # NOTE: Each Disjoint set is uniquely identified by its root
            # For each disjoint set, how many val=v does it contain
            # for each disjoint set, to compute #paths for [v] := 1 + 2 + ... + n  // where n is number of node with v in disjoint set
            count = defaultdict(int)
            for i in idxs:
                root = uf.find(i)
                count[root] += 1
                res += count[root]  # res will be accumulated 
            
        return res

                         
                    




