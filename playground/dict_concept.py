from itertools import count
from collections import defaultdict

def values_to_count():

    d = {1:1, 2:2, 3:2, 4:4, 40:4, 5:5}
    l = zip(set(d.values()), count())
    m = dict(l)

    print(m)

def defaultdict_and_cntr():
    cntr = count()

    posAllocater = defaultdict(cntr.__next__)

    d = [1, 2, 1, 3, 2, 4]
    m = [0]*4

    for n in d:
        pos = posAllocater[n]
        m[pos] += 1
    
    print(posAllocater)
    print(m)

defaultdict_and_cntr()
