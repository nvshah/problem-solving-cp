# https://leetcode.com/problems/bus-routes/description/
from typing import List
from collections import defaultdict, deque
'''
routes : 
idx -> #bus, 
val -> bus-stops 
'''

# O(stops) time | O(stops) space  }-> stops = bus * routes
def numBusesToDestination(routes: List[List[int]], source: int, target: int) -> int:
    # buses passing through given busStop
    if source == target: return 0

    busStopBuses = defaultdict(list) # busStop -> [busNo]

    for busNo, busStops in enumerate(routes):
        for stop in busStops:
            busStopBuses[stop].append(busNo)

    visitedBuses = set() 
    visitedStops = set()

    que = deque() # (busStop, busesTravelled)
    que.append((source, 0))

    while que:
        stop, numBusesChanged = que.popleft() 

        if stop == target:
            return numBusesChanged # total buses changed

        buses = busStopBuses[stop]

        for busId in buses:
            if busId in visitedBuses: continue
            visitedBuses.add(busId) # Explore via taking [busId]
            for stop in routes[busId]:
                if stop in visitedStops: continue 
                visitedStops.add(stop)
                que.append((stop, numBusesChanged + 1)) # Upcoming possible [stp]
    
    return -1
            
                

        
        

