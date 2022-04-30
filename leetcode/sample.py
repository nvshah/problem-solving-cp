from collections import defaultdict, Counter
import itertools as it
import heapq 


# Sorted
l = [(1, 0), (1, 2), (2, 0), (2, 3)]

d_l2 = defaultdict(int)

for e in l:
    d_l2[e[0]] = max(d_l2[e[0]], e[1])

print(d_l2)

print(heapq.nlargest(3, [1, 4, 5, -1, 3, 10, 12]))

h = [3, 2, 5]
heapq.heapify(h)
print(h)
heapq.heapreplace(h, 10)
print(h)

s1 = 'ama'
s2 = 'maa'

print(Counter(s1) == Counter(s2))





