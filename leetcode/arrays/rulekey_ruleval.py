from typing import List
from functools import reduce
from enum import auto

# https://leetcode.com/problems/count-items-matching-a-rule/


def countMatches(items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
    i = 0
    if ruleKey == "color":
        i = 1
    elif ruleKey == "name":
        i = 2

    def reduceFunc(x, y):
        return x + (y[i] == ruleValue)

    return reduce(reduceFunc, items, 0)


def countMatches2(items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
    i = 0
    if ruleKey == "color":
        i = 1
    elif ruleKey == "name":
        i = 2

    t = 0
    for item in items:
        if item[i] == ruleValue:
            t += 1
    return t


items = [["phone", "blue", "pixel"], ["computer",
                                      "silver", "lenovo"], ["phone", "gold", "iphone"]]
ruleKey = "color"
ruleValue = "silver"

items = [["phone", "blue", "pixel"], ["computer",
                                      "silver", "phone"], ["phone", "gold", "iphone"]]
ruleKey = "type"
ruleValue = "phone"

ans = countMatches(items=items, ruleKey=ruleKey, ruleValue=ruleValue)

print(ans)
