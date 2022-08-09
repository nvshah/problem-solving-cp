# https://leetcode.com/problems/task-scheduler/
from typing import List
from collections import Counter, deque
import heapq

'''
QUE
Given a characters array tasks, representing the tasks a CPU needs to do, 
where each letter represents a different task. Tasks could be done in any order. 
Each task is done in one unit of time.

For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks 
(the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.
'''

def leastInterval(tasks: List[str], n: int) -> int:
    ''' O(n*m)n :=  '''
    # each task takes 1 unit of time

    counts = Counter(tasks)
    # create max heaps of count values
    maxHeap = [-cnt for cnt in counts.values()]
    heapq.heapify(maxHeap)

    time = 0
    # use to holds the task in timeline fashion 
    # ( which can be added into max heap later )
    q = deque()  # [cnt, coolDownEndTime]

    while maxHeap or q:
        time += 1

        # Account a character with max count from max heap
        if maxHeap:
            cnt = -heapq.heappop(maxHeap)  # - to get actual count
            if cnt-1!=0:
                q.append((cnt-1, time+n))
        
        # Check if any task cooldown period overs after this [time]
        if q and q[0][1] == time:
            cnt, _ = q.popleft()
            heapq.heappush(maxHeap, -cnt)
    
    return time
