'''
The submarine seems to already have a planned course (your puzzle input). You should probably figure out where it's going. For example:

down X increases your aim by X units.
up X decreases your aim by X units.
forward X does two things:
It increases your horizontal position by X units.
It increases your depth by your aim multiplied by X.
'''

with open('advent of code/d2_puzzle_input.txt') as f:
    h = v = aim = 0
    for i in f:
        s = i.strip().split()
        n = int(s[1])
        if s[0][0] == 'f':    # forwards
            h += n
            v += aim*n
        elif s[0][0] == 'd':  # downawards
            aim += n 
        else:  # upwards
            aim -= n
        #print(h, v)
    print(h * v) # ans = 2015547716
