# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/

class UnionFind:
    def __init__(self, stones):
        # Each Row & Column in the Plane will be treated as a Parent at init
        parent = {}   # parent map, int (group) -> int (parent)
        for x, y in stones:
            # current stone (in 2D) := Half stone in X axis + other Half in Y axis
            #                          So Single Stone may belongs to 2 diff parent
            # Inorder to distinguish row & col as seperate using -ve sign for row & +ve for col
            r, c = -(x + 1), y+1   # +1 inorder to avoid 0
            parent[r] = r 
            parent[c] = c 

        self.parent_map = parent
        self.totalGrps = len(parent)

    def find(self, k): # k := coordinate offset in single direction (ie x or y) 
        '''Find the parent for coordinate offset {k}'''
        # If self is Parent i.e := it is Parent of the entailing group
        if self.parent_map[k] != k:
            # As this is recursive so it will cover the Path Compression as well
            self.parent_map[k] = self.find(self.parent_map[k]) 
        return self.parent_map[k]
    
    def union(self, x, y):
        ''' merge the 2 possible group (if any) by 2 direction axis x & y resp. '''
        par_x = self.find(x) 
        par_y = self.find(y) 

        if par_x == par_y:  # {x} & {y} already belongs to same group
            return 

        # Reduce by 1 grp (because of absolute merge)
        self.totalGrps -= 1
        
        # Here we know that x & y are integral part of stone
        #  so they would be always connected So perform merge
        self.parent_map[par_y] = par_x


class Solution:
    def removeStones(self, stones):
        uf = UnionFind(stones)
        for x, y in stones:
            uf.union(-x-1, y+1) # adding +1 inorder avoid (0, 0)
        return len(stones) - uf.totalGrps


class Solution2:
    def removeStones(self, stones):
        
        ### UF is a hash map where you can find the root of a group of elements giving an element.
        ### A key in UF is a element, UF[x] is x's parent.
        ### If UF[x] == x meaning x is the root of its group.
        UF = {}
        
        ### Given an element, find the root of the group to which this element belongs.
        def find(x):
            
            ### If x == UF[x], meaning x is the root of this group.
            ### If x != UF[x], we use the find function again on x's parent UF[x] 
            ### until we find the root and set it as the parent (value) of x in UF.
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        ### Given two elements x and y, we know that x and y should be in the same group, 
        ### this means the group that contains x and the group that contains y 
        ### should be merged together if they are currently separate groups.
        ### So we first find the root of x and the root of y using the find function.
        ### We then set the root of y (rootY) as the root of the root of x (rootX).
        def union(x, y):
            
            ### this may be the first time we see x or y, so set itself as the root.
            if x not in UF:
                UF[x] = x
            if y not in UF:
                UF[y] = y
            rootX = find(x)
            rootY = find(y)
            # set the root of y (rootY) as the root of the root of x (rootX)
            UF[rootX] = rootY
        
        ### The main reason we can use the union-find algorithm here is that we treat the x and y of each stone as a single element!
        ### DO NOT think of a stone as (x,y); instead, think about one stone as two elements, x and y!
        ### Now, a stone means two elements, x and y, that are CONNECTED.
        ### Since x and y can be the same, but 0 <= x, y <= 10^4, we can add 10^4 to every y 
        ### to distinguish x and y and treat them as different elements.
        ### We can go to every pair of x and y (a stone), we know that x and y should be in 
        ### the same group, so we union them.
        maxX = 10**4
        for x,y in stones:
            union(x,y+maxX)
        
        ### Finally, we go through each element in UF and find their root, count how many 
        ### connected components (unique roots) are there and subtract it from the total 
        ### number of stones.
        return len(stones) - len({find(n) for n in UF})

if __name__ == '__main__':
    stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    ans = Solution()
    out = ans.removeStones(stones)
    print(out)