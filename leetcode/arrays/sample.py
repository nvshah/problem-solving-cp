import itertools as it
from typing import List

l = [*it.product([1,2,3], [4,5,6])]

print(l)

#print((i for i in range(2)) + (i for i in range(4))) 
