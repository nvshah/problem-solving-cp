# https://leetcode.com/problems/largest-submatrix-with-rearrangements
from typing import List 

def largestSubmatrix(matrix: List[List[int]]) -> int:
    M, N = len(matrix), len(matrix[0])

    prefix_heights = [0]*N  # prevRow (continuous vertical line)

    area = 0 # max area

    for r in range(M):
        cur_row = matrix[r]

        # accumulated col prefix
        #prefix_heights = [(cur + prev) if cur else 0 for (prev, cur) in zip(prefix_heights, cur_row)]
        for i in range(N):
            if cur_row[i]:
                prefix_heights[i] += cur_row[i]
            else:
                prefix_heights[i] = 0

        # Sort to get decreasing Bar Plot like graph
        adjusted_heights = sorted(prefix_heights, reverse=True)

        for i in range(N):
            height, width = adjusted_heights[i], i+1
            area = max(area, height * width) # area
    
    return area


# TEST

m = [[1,1,0], [1,0,1]]
ans = largestSubmatrix(m)
print(ans)