# https://leetcode.com/problems/baseball-game/
from typing import List

def calPoints(ops: List[str]) -> int:
    stack = []
    for op in ops:
        match op:
            case "+":
                stack.append(stack[-1] + stack[-2])
            case "D":
                stack.append(stack[-1]*2)
            case "C":
                stack.pop()
            case num:
                stack.append(int(num))

    return sum(stack)

ops = ["5","2","C","D","+"]
a = calPoints(ops)
print(a)