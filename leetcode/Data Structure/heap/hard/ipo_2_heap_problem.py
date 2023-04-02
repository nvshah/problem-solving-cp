# https://leetcode.com/problems/ipo/submissions/

'''
Better Problem

2 Heaps Problem
Logics : MinHeap + MaxHeap  // Used in same problem

'''

from typing import List
import heapq

def findMaximizedCapital(k: int, w: int, profits: List[int], capital: List[int]) -> int:
    # Max Heap (prioroty queue) | keep tracks of profits that can be picked at moment
    max_profit = []   # affordable profits only

    # Min Heap (priority queue) so as to pick next optimal candidate inorder to send to [max_profit] heap !
    # Keeps tracks of next possible candidates for [max_profit]
    min_capital = [(c, p) for c, p in zip(capital, profits)]  # (capital, profit)
    heapq.heapify(min_capital)

    for i in range(k):

        # get all next possible candidates for affordable profits from [min_capital]
        while min_capital and min_capital[0][0] <= w:
            _, prof = heapq.heappop(min_capital)
            heapq.heappush(max_profit, -prof)  # adding `-` as its max-heap 

        # check if there exists any profits to be picked
        if not max_profit:
            break

        # get optimal profit
        w += -heapq.heappop(max_profit)  # # adding `-` as its max-heap 

    return w
    