# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
from typing import List

'''
Idea
We will try to find the min and max weight/load we carry per ship (ie per day)
hence we aim to find lower & upper bound of weight-load per ship if possible

Thus with lower & upper bound we've our search-space
Also
As we have bounds, so we can use Binary Search to find correct/ideal weight

T.C :=
// consider n as the #count of items to be carried
Best case := carry `maximal weight` per ship  // 1 (smallest weight per ship)
Worst case := carry `total weight` per ship   // 500*n (largest weight per ship)

let (500*n) be K,
Hence binary search for search space of `K` items would be `logK` 

Now for each candidate in binary search we will iterate over all items to check if capacity is suffice or not !
hence 1 -> n
      logK -> ?

      (n * logK) => is the avg T.C 

      [Avg Time Complexity as search space will gradually decrease as iteration proceeds]

'''

def shipWithinDays(weights: List[int], days: int) -> int:
    # LOWER-BOUND
    # Ideally ship should carry atleast 1 item per day, so 
    # minimum weight it needs to carry := max(weights)

    # UPPER-BOUND
    # In Worst case ship can carry all items per day (ie all items in 1 day/ship)
    # maximum weight it can carry := sum(weights)
    # Hence ship can carry atmost {sum(weights)}

    l = max(weights) # lower bound }-> atleast 1 item per ship
    r = sum(weights) # upper bound }-> all items per ship

    capacity = r  # Worst case (all items in 1 day) | Simplest Solution | Underfittig
    # GOAL :- find the least possible {capacity} value

    def canShip(cap):
        '''
           check if all items can be loaded when ship's max capacity is [cap]
        '''
        ships = 1 # as we know atleast 1 ship will be used to carry items
        curCap = cap # current capacity of ship

        for w in weights:
            if curCap < w: 
                # require new fresh ship as item with weight [w] cant be load into cur-ship
                ships += 1
                curCap = cap 
            # load item into cur-ship
            curCap -= w
        return ships <= days  # as per day only 1 ship gonna shipped !

    # Perform binary search in search-space over [l, r]
    while l <= r:
        m = (l+r) // 2
        if canShip(m):
            # update optimal capacity
            capacity = min(capacity, m)
            # Try to find even smaller capacity than {cap}
            r = m-1
        else:
            # Can't ship with {cap} capacity so need to increase capacity per ship
            l = m+1
    
    return capacity