from functools import partial
from operator import and_
from itertools import accumulate

def test0():
    l = [1,2,3,4,5,6]
    l = [2,4,6,8]
    i = filter(partial(and_, 1), l) # Odd Nums
    f = next(i, None) 
    s = next(i, None)



    print(f, s)

def test1():
    *k, = accumulate(range(1, 5), lambda x, y: y , initial=10)
    print(k) 

test1()


