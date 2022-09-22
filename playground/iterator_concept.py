from functools import partial
from operator import and_


l = [1,2,3,4,5,6]
l = [2,4,6,8]
i = filter(partial(and_, 1), l) # Odd Nums
f = next(i, None) 
s = next(i, None)

print(f, s)
