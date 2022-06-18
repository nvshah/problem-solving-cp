# https://leetcode.com/problems/course-schedule-ii/
from typing import List

'''
QUE

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return the ordering of courses you should take to finish all courses. 
If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

'''

'''
IDEA : Topological Sort
'''

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    # 1. create map for each course & its pre-requisites
    #    course -> [courses]
    coursePrereq = {c: [] for c in range(numCourses)}
    for c, p in prerequisites:  # course, pre-req
        coursePrereq[c].append(p)

    # 2. DFS (For checking Course Completion)
    visit = set()  # track all courses required for curr-course
    # ! This order need not be unique
    order = [] # course to complete in order
    
    completed = set()  # set of course completed so far

    # 3. DFS
    def dfs(c):  # c := course
        if c in visit:
            return False  # Detected Loop
        if c in completed:
            return True  # no pre-requisites (ie completed)

        # start the course
        visit.add(c)
        
        for p in coursePrereq[c]:
            status = dfs(p)
            if not status:
                return False  # as {p} is not completed {c} cannot be completed
        
        # All prereq completed now you can start this course {c}
        order.append(c)
        
        visit.remove(c)
        # complete the course
        completed.add(c)

        return True

    # 4. Check Lazily
    allFinish = all(dfs(i) for i in range(numCourses))
    return order if allFinish else []