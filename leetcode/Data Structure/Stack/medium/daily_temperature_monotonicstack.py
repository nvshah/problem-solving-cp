# https://leetcode.com/problems/daily-temperatures/

"""
Idea :- Monotonic Decreasing Stack 

"""
from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    ans = [0] * len(temperatures)
    stack = []  # element -> (temperature, index)

    for i, t in enumerate(temperatures):
        # 1. Check Monotonic Decreasing Property (considering new temperature {t})
        while stack and t > stack[-1][0]:
            # found the warmer day for recent elem on stack
            recentTemp, recentIdx = stack.pop()
            ans[recentIdx] = i - recentIdx  # storing answer
        stack.append((t, i))  # add curr temp entry to stack

    return ans


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
temperatures = [30, 40, 50, 60]
temperatures = [30, 60, 90]
ans = dailyTemperatures(temperatures)
print(ans)
