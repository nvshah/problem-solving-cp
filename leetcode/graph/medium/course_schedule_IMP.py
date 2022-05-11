# https://leetcode.com/problems/course-schedule/

'''
Que
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.
'''

from typing import List

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # 1. create map for each course & its pre-requisites
    #    course -> [courses]
    coursePrereq = {c: [] for c in range(numCourses)}
    for c, p in prerequisites:  # course, pre-req
        coursePrereq[c].append(p)

    # 2. DFS (For checking Course Completion)
    visit = set()  # track all courses required for curr-course

    # 3. DFS
    def dfs(c):  # c := course
        if c in visit:
            return False  # Detected Loop
        if not coursePrereq[c]:
            return True  # no pre-requisites (ie completed)

        # start the course
        visit.add(c)

        for p in coursePrereq[c]:
            status = dfs(p)
            if not status:
                return False  # as {p} is not completed {c} cannot be completed

        # complete the course
        visit.remove(c)
        # as this course is completed already so there not exists any pre-req anymore for this course
        # so next time it can be directly hinted as completed (ie no pre-requisite)
        coursePrereq[c] = []

        return True

    # 4. Check Lazily
    allFinish = all(dfs(i) for i in range(numCourses))
    return allFinish