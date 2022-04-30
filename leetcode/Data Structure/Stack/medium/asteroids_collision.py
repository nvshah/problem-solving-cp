# https://leetcode.com/problems/asteroid-collision/
from typing import List

def asteroidCollision(asteroids: List[int]) -> List[int]:
    stack = [] # keep track of asteroids after collision if happend

    #* Collision will happen only when 2 asteroid move in diff dir s.t -> <-
    #  ie Right Left Scenario

    for a in asteroids:
        #1. check for collision
        #   Collision := asteriod on top of stack is moving right & asteroid {a} is moving left
        while stack and a < 0 and stack[-1] > 0:
            # Collision between {a} & {top}
            aftermath = a + stack[-1]
            if aftermath < 0: 
                # Left asteroid (ie on top of stack & movinng in right dir) explode
                stack.pop()   # thus remove it from stack
            elif aftermath > 0: 
                # right one explode  (ie mmoving in left direction)
                a = 0  # 0 := no asteroid
            else:
                # Both explodes
                a = 0 
                stack.pop() 

        if a:
            stack.append(a)  # if {a} is not exploded

    return stack



