# https://leetcode.com/problems/queue-reconstruction-by-height/

from typing import List


def reconstructQueue(people: List[List[int]]) -> List[List[int]]:
    people.sort(key= lambda x: (x[0], -x[1]))
    n = len(people)
    queue = [None]*n
    cnts = [-1]*n
    for h, k in people:
        front = -1
        for i in range(n):
            if not queue[i] or queue[i][0] == h:  # As prev added elem can be <= current height
                front += 1
            if front == k:
                break
        queue[i] = [h, k]
    return queue