

from bisect import bisect_left
from operator import itemgetter

'''Task : To check if interval is not overlapping with existing one on addition'''

class MyCalendar:

    def __init__(self):
        MAX = 10**9
        self.events = [(-1,-1), (MAX, MAX)]
        

    def book(self, start: int, end: int) -> bool:
        # binary search to find the end time -> compare cur's [end] with existing's [start]
        pos = bisect_left(self.events, end, key=itemgetter(0))
        if self.events[pos-1] > start:  # Overlapping between prev & current
            return False
        self.events.insert(pos, (start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)