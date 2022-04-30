'''
Sum of each 3 measurement window
'''

from collections import deque


with open('./advent of code/puzzle_1_input.txt') as f:
    cntr = 0
    window = deque()
    for i in range(3):
        l = int(next(f).strip())  # point to first in window
        window.append(l)

    for l in f:
        n = int(l.strip())
        cntr += n > window[0]
        window.popleft()
        window.append(n)
    print(cntr)  # 