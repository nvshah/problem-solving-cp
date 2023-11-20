# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
from typing import List
from bisect import bisect

class Solution:

    def minCost(self, n: int, cuts: List[int]) -> int:
        '''Dp Top-Down | Memoziing'''
        cache = {}

        INF = float('inf')

        def dfs(l, r):
            '''left & right end of current scale'''
            if l > r: return 0
            if (l,r) in cache: return cache[(l,r)]

            res = INF 
            for c in cuts:
                if l < c < r: # c is effective cut dividing current scale
                    res = min(
                        res, 
                        r-l + dfs(l, c) + dfs(c, r)
                    )
            if res == INF: return 0 
            cache[(l,r)] = res 
            return res 

        return dfs(0, n)



# def minCost(n: int, cuts: List[int]) -> int:
#     '''Not passed all Cases'''
#     marks = sorted(cuts) 

#     def perform(s, e, points):
#         if not points: return 0

#         middle = (s + e) // 2

#         m = -1
#         if len(points) & 1: # odd 
#             m = (len(points)-1) // 2
#         else: # even 
#             l = (len(points)-1) // 2 
#             m = l 
#             if (l+1 < len(points)) and (abs(middle - points[l]) > abs(middle - points[l+1])):
#                 m = l+1

#         # i = bisect(points, middle)
#         # m = -1 
#         # d = len(points)+1
#         # if i < len(points):
#         #     if points[i]-middle < d:
#         #         m = i
#         #         d = points[i]-middle
#         # if i > 0:
#         #     if middle-points[i-1] < d:
#         #         m = i-1

#         p = points[m]

#         if s == p or e == p: return 0

#         left = perform(s, p, points[:m])
#         right = perform(p, e, points[m+1:])

#         #print('Performed -> ', s, e, left, right)

#         return e-s + left + right 

#     return perform(0, n, marks)

n = 7
c = [1,3,4,5]

# n = 9
# c = [5,6,1,4,2]

ans = minCost(n, c)
print(ans)