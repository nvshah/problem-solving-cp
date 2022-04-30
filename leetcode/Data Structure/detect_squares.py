# https://leetcode.com/problems/detect-squares/

from collections import defaultdict
from typing import List

class DetectSquares:

    def __init__(self):
        self.ptsFreq = defaultdict(int)
        self.pts = []
        
    def add(self, point: List[int]) -> None:
        self.pts.append(point)
        self.ptsFreq[(*point,)] += 1  # update freq count of this point

    def count(self, point: List[int]) -> int:
        px, py = point # x & y corrdinate
        cnt = 0
        
        for x, y in self.pts:
            # 1. check diagonal option from available points to this given point
            if abs(px-x) == abs(py-y):
                # 2. Check if distance on diagonal axis between (x,y) & (px,py) is > 0
                if px != x :  # (py != y) also gets true (as both distance are same)
                    # Found 2 point of Possible square i.e (x,y) & (px,py)
                    # need to find 2 more points (x, py) & (px, y)
                    cnt += self.ptsFreq[(x, py)] * self.ptsFreq[(px, y)]
        
        return cnt
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)