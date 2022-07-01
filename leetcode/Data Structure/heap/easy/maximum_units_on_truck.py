# https://leetcode.com/problems/maximum-units-on-a-truck/submissions/


from heapq import heapify, heappop
from typing import List


def maximumUnits(boxTypes: List[List[int]], truckSize: int) -> int:
    '''Heap O(n*logn) Worst Case 
    '''
    amount = 0
    # Inorder to make Max-Heap of #Units
    hp = [(-units, count) for count, units in boxTypes]
    heapify(hp)

    while hp and truckSize > 0:
        units, count = heappop(hp)
        putCount = min(count, truckSize)  # num of boxes to put in truck
        amount += putCount * -units  # total units to put
        truckSize -= putCount  # kept & lowered the capacity

    return amount

def maximumUnits2(boxTypes: List[List[int]], truckSize: int) -> int:
    ''' Sort O(n*logn)'''   
    boxTypes.sort(key=lambda x: -x[1])
    capacity = 0
    
    for box, unit in boxTypes:
        if truckSize >= box:
            truckSize -= box
            capacity += box*unit
        else:
            capacity += truckSize*unit
            break
    
    return capacity
        
            