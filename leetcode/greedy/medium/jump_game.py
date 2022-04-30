# https://leetcode.com/problems/jump-game/

from typing import List

def canJump(nums: List[int]) -> bool:
    ''' Greedy Soln (Explore from End -> Start) | O(n) '''
    size = len(nums)
    goal = size - 1  # last idx is goal

    for i in range(size-1, -1, -1):
        if i + nums[i] >= goal:  # can we make jump from {i} to {goal}
            goal = i  # Shift goal to curr pos as we can jumpr from {i} -> {goal}
        
    return goal == 0

def canJump2(nums: List[int]) -> bool:
    ''' Valley Peak Approach '''
    size = len(nums)
    reachable = 0

    for i in range(size):
        if reachable >= size-1:  # surpasses last index
            print('Quit')
            return True

        if reachable < i:  # as we cannot reach to current {i} So we cannot move ahead as well
            return False
        
        reachable = max(reachable, i + nums[i])  # How far can we jump from curr {i}
    
    return True

nums = [2,3,1,1,4]
#nums = [3,2,1,0,4]

print(canJump2(nums))

