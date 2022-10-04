# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

from itertools import takewhile
from typing import List


def minCost(colors: str, neededTime: List[int]) -> int:
    prev_color, prev_time = colors[0], neededTime[0]

    ans = 0
    for i in range(1, len(colors)):
        color, time = colors[i], neededTime[i]

        if color == prev_color:
            if time > prev_time: 
                ans += prev_time
                prev_time = time  # new time
            else:
                ans += time # better time
        else:
            prev_color, prev_time = color, time  # First member of new color

    return ans

            

colors = "abaac"
neededTime = [1,2,3,4,5]

ans = minCost(colors, neededTime)