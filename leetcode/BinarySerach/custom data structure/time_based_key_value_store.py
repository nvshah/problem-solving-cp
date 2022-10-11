# https://leetcode.com/problems/time-based-key-value-store/

import bisect
from collections import defaultdict
from operator import itemgetter
from typing import Collection


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)  # key : list of [val, time]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.store[key]
        if not lst: return ""
        
        # Bisect the RHS Index
        i = bisect.bisect(lst, timestamp, key=itemgetter(1)) # pos i just after ideal candidate
        if not i: return ""  # not found time s.t time <= timestamp

        return lst[i-1][0]  # ideal time_prev will reside at position i-1
