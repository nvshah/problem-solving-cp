# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

*t, = map(int, input().split())

print(np.vectorize(int)(np.zeros(t)).reshape(t))
print(np.vectorize(int)(np.ones(t)).reshape(t))
