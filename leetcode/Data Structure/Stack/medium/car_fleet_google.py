# https://leetcode.com/problems/car-fleet/

from typing import List

def calculate_time(d, s):
    ''' speed = distance/time '''
    return d / s

def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    '''
     1) Sort the cars in order of their distance positionns
     2) Start from the car that is nearest to target i.r From RHS -> LHS

    '''
    stack = []
    # for every car(pos, speed) sort cars according to their position in descending order
    cars = sorted(zip(position, speed), reverse=True)
    stack.append(calculate_time(target - cars[0][0], cars[0][1]))  # add time of nearest car to target
    for p, s in cars[1:]:
        time = calculate_time(target-p, s)
        if time > stack[-1]:
            # new benchmark
            stack.append(time)

    return len(stack)

def carFleet2(target: int, position: List[int], speed: List[int]) -> int:
    '''
     1) Sort the cars in order of their distance positionns
     2) Start from the car that is nearest to target i.r From RHS -> LHS

    '''
    prev_car_time, fleet = 0, 1
    # for every car(pos, speed) sort cars according to their position in descending order
    cars = sorted(zip(position, speed), reverse=True)
    prev_car_time = calculate_time(target - cars[0][0], cars[0][1])  # add time of nearest car to target
    for p, s in cars[1:]:
        time = calculate_time(target-p, s)
        if time > prev_car_time:
            # new benchmark = new fleet
            prev_car_time, fleet = time, fleet+1 
            
    return fleet


target = 12
position = [10,8,0,5,3] 
speed = [2,4,1,1,3]

# target = 10
# position = [3]
# speed = [3]


print(carFleet(target, position, speed))
