# https://leetcode.com/problems/jump-game-ii/

from typing import List

def jump(nums: List[int]) -> int:
    ''' Approach Greedy + Level by level Explore '''
    jumps = 0  # total jumps performed
    l = r = 0  # representing current window(level)

    #! Assumption :- We can always reach the last index (Given)
    while r < len(nums)-1:  # till not reach at last position

        # 1. Find the farthest position that can be reach from current window
        farthest = max(nums[i] + i for i in range(l, r+1))

        # 2. get next Window
        l = r+1  # from assumption (we can move to next window atleast)
        r = farthest

        # 3. Make Jump to next Window
        jumps += 1

    return jumps

nums = [2,3,1,1,4]  # 2

nums = [2,3,0,1,4]

js = jump(nums)


print(js)