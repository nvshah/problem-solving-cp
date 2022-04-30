# https://leetcode.com/problems/single-threaded-cpu/

from typing import List
import heapq

'''
Task :- [enqueTime, processingTime]
'''

def getOrder(tasks: List[List[int]]) -> List[int]:
    size = len(tasks)
    # 1. Get the index for sorted tasks based on enque time (ie simulate argsort())
    tasksIdx = sorted(range(size), key=tasks.__getitem__)

    #print(tasksIdx)

    seq = []  # task's {idx} entry in ideal sequence (scheduled final array)

    # 2 mark the currTime (ir starting time) as the first task in order
    currTime = tasks[tasksIdx[0]][0]

    # 3. Schedule all tasks
    i = 0
    priorityQ = []  # Priority Queue := Min Heap
    while i < size:  # till all tasks are not scheduled
        # 3.1 Add all the eligible tasks to QUEUE
        currTaskIdx = tasksIdx[i]
        currTask = tasks[currTaskIdx]
        if currTime >= currTask[0]:  # ADD Tasks
            heapq.heappush(priorityQ, (currTask[1], currTaskIdx)) # adding (processTime, index) to heap as enntry
            i += 1 # move to next task in order
        # 3.2 Schedule TASKS
        else:
            if priorityQ: # any tasks are waiting in queue
                processTime, idx = heapq.heappop(priorityQ)  # select 1 with high priority (ie less Processing Time)
                currTime += processTime # finish the current executing task (highest preferred task := one at root in min-heap)
                seq.append(idx)
            else:
                # no tasks being waiting to be executed
                # let next task be scheduled thus directly
                currTime = currTask[0]  # NOTE -> i is pointing to next possible task's index to add into QUeue
    
    #print(priorityQ)
    # 4. Empty Queue & Schedule Tasks 1 by 1
    while priorityQ:  
        processTime, idx = heapq.heappop(priorityQ)  # select 1 with high priority (ie less Processing Time)
        seq.append(idx)
            
    return seq

def getOrder2(tasks: List[List[int]]) -> List[int]:
    # 1. Append the idx to all task as well as we gonna need it while preparing ans
    for i, t in enumerate(tasks):
        t.append(i)

    # Thus single task := [enqueTime, processTime, idx]

    # 2. sort the tasks based on their enqueing time    
    tasks.sort()

    # 3. initialize necessary things
    i, size = 0, len(tasks)
    curTime = tasks[0][0]
    res = []
    minHeap = []  # Priority Queue // will hold tasks in appropriate order

    # 4. Queue & Schedule
    while minHeap or i < size:  # Till all tasks are scheduled

        # 4.1 Add the tasks to Queue
        while i < size and curTime >= tasks[i][0]:
            heapq.heappush(minHeap, (tasks[i][1], tasks[i][2]))  # item := (processTime, idx)  // we do not require startTime/enqueTime
            i += 1 
        
        # 4.2 Schedule the task
        if minHeap:
            # complete the runninng task
            procTime, idx = heapq.heappop(minHeap)
            res.append(idx)  # Task at {idx} ie tasks[idx] is completed
            curTime += procTime  # time elapsed to complete current task ie task[idx]
        else:
            # No task is waiting in Queue So Start next available task
            nextTask = tasks[i]
            curTime = nextTask[0]  # tick cur time to next task enque time

    return res


tasks = [[1,2],[2,4],[3,2],[4,1]]  #  [0, 2, 3, 1]

tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]  # [4,3,2,0,1]

ans = getOrder(tasks)

print(ans)