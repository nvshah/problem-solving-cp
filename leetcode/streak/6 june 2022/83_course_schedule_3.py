# https://leetcode.com/problems/course-schedule-iii/
from operator import itemgetter
from heapq import heappush, heappop
from typing import List

def scheduleCourse(courses: List[List[int]]) -> int:
    courses.sort(key=itemgetter(1))  # According to timeline (ie increasing timielimits)
    
    maxHp = []
    time = 0
    for dur, end in courses:
        heappush(maxHp, -dur)  # Take this Course
        time += dur
        if time > end:         # Reject the Course Which is lengthiest (from currently taken ones)
            big_dur = -heappop(maxHp)
            time -= big_dur
    
    return len(maxHp)