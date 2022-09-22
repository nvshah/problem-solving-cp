from functools import partial
from operator import and_ 

*a, = filter(partial(and_, 1), [1,2,34, 33])

print(a)