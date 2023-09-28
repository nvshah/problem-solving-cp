#https://leetcode.com/problems/data-stream-as-disjoint-intervals/
from sortedcontainers import SortedSet
from typing import List

class SummaryRanges:

    def __init__(self):
        # treeSet is used specially to optimize the adding of element in sorted manner. (ie o(log(n)))
        # SortedSet => implemented using Binary Tree Structure
        self.treeSet = SortedSet()

    def addNum(self, value: int) -> None:
        self.treeSet.add(value)

    def getIntervals(self) -> List[List[int]]:
        res = [[-2, -2]] # (start, end) range // (-1, -1 dummy range)
        for n in self.treeSet:
            if res[-1][-1] + 1 == n:
                # new end found
                res[-1][-1] = n 
            else:
                res.append([n, n])
        del res[0] # remove dummy 
        return res

        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()