# https://leetcode.com/problems/path-with-minimum-effort/
from typing import List
import heapq as hq


def minimumEffortPath(heights: List[List[int]]) -> int:
        ''' Idea : 
            Kinda DijkStras Algo
            BFS (Via Heap | Priority queue)
        '''
        m, n = len(heights), len(heights[0])
        inf = float('inf')
        
        hp = [(0, 0, 0)]  # (effort, row, col)
        efforts = [
            [inf]*n
            for _ in range(m)
        ]
        
        while hp:
            ef, r, c = hq.heappop(hp)
            
            if r == m-1 and c == n-1:  # reach dest (bottom right)
                return ef
            
            cur = heights[r][c]
            
            # 1. Find max abs dev for all neighbors
            for x, y in ((0,1), (1, 0), (0, -1), (-1, 0)):
                nx, ny = r+x, c+y
                if 0 <= nx < m and 0 <= ny < n:
                    # find the maximal effort from cur
                    nxt = heights[nx][ny]
                    ne = max(abs(cur - nxt), ef) # calc efforts
                    
                    # check if this new cell(nx, ny) is useful
                    if ne < efforts[nx][ny]:
                        efforts[nx][ny] = ne
                        hq.heappush(hp, (ne, nx, ny))