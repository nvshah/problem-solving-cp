# https://leetcode.com/problems/design-underground-system/
from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        # travel start flag
        self.entry = {}   # int : (int, string, int)  // id -> entity
        self.totalTime = defaultdict(int) # str : int  // travel -> time
        self.cnts = defaultdict(int) # str : int // travel -> freqs
        
    def get_key(self, start, end):
        return f'{start}-{end}'
    
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.entry[id] = (id, stationName, t)  # register the start station for {id}

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        _, s, t1 = self.entry.pop(id)  
        d = t - t1
        k = self.get_key(s, stationName)
        
        # Update time & freqs for this travel (ie s -> stationName)
        self.totalTime[k] += d
        self.cnts[k] += 1
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        k = self.get_key(startStation, endStation)
        return self.totalTime[k] / self.cnts[k]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)