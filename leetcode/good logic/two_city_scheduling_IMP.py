# https://leetcode.com/problems/two-city-scheduling/
from typing import List
import operator as op

def twoCitySchedCost(costs: List[List[int]]) -> int:
    '''
    Idea : The Population belonging at larger extent to certain favourable group will be given low priority
           For Eg
            For A -> the the pair that have smaller diff of (a-b) is prefeerred first for A' group
                B -> The pair that have smallest diff of (b-a) is given priority for B's group First

                b-a = -(a-b)

           Other Perspective :-
             Take those Pairs first for A, where B is dominating to A in larger extent
                  those Pairs first for B, where A is dominating to B in larger extent
    '''
    n = len(costs) // 2
    # {diffs} := between b & a ie (b-a)
    # Thus first n of diffs will go to B -> diffs[:n]
    # & remaining to A -> diffs[n:]
    diffs = sorted(costs, key=lambda c: c[1] - c[0])
    res = sum(map(op.itemgetter(1), diffs[:n])) + sum(map(op.itemgetter(0), diffs[n:]))
    return res
