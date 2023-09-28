import itertools as it 
from operator import not_

def check1():
    a = iter([1,4,10,14,20,27,30])
    k = it.dropwhile(lambda x: x<12, a)
    f = next(k)
    print(f)

def check2():
    t = iter([1,2,13,0,0,0,4,5,6,0,0])
    t = it.dropwhile(bool, t)
    #print(list(r1))  // [0, 0, 0, 4, 5, 6, 0, 0]
    r2 = it.takewhile(not_, t)
    #print(list(r2))
    print(list(t))

def check3():
    t = iter([1,2,3,0,4,5,6,70,8,9])
    t1 = it.takewhile(bool, t)
    t2 = it.takewhile(bool, t)
    print(list(t1))
    print([*t2])

if __name__ == '__main__':
    check3()
