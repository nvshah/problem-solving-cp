'''
Task find the number of counts that are larger than prev numbers
'''

with open('./advent of code/puzzle_1_input.txt') as f:
    prev = 0
    cntr = 0
    prev = int(next(f).strip())  # skip first
    for l in f:
        n = int(l.strip())
        print(n, prev)
        cntr += n > prev
        prev = n
    print(cntr)  # ans = 1715
