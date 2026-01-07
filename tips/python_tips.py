from collections import deque
from itertools import repeat


# Do some work repeteadly without using for loop
def perform_task(task, ntimes):
    deque(repeat(task(), ntimes), maxlen=0)
