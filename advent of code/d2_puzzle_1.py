'''
The submarine seems to already have a planned course (your puzzle input). You should probably figure out where it's going. For example:

forward 5
down 5
forward 8
up 3
down 8
forward 2
Your horizontal position and depth both start at 0. The steps above would then modify them as follows:

forward 5 adds 5 to your horizontal position, a total of 5.
down 5 adds 5 to your depth, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13.
up 3 decreases your depth by 3, resulting in a value of 2.
down 8 adds 8 to your depth, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15.
After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)
'''

with open('advent of code/d2_puzzle_input.txt') as f:
    h, v = 0, 0
    for i in f:
        s = i.strip().split()
        print(s)
        if s[0][0] == 'f':    # forwards
            h += int(s[1])
        elif s[0][0] == 'd':  # downawards
            v += int(s[1])
        else:  # upwards
            v -= int(s[1])
        #print(h, v)
    print(h * v) # ans = 2036120
