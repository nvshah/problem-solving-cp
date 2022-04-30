import itertools as it 

a = iter([1,4,10,14,20,27,30])
k = it.dropwhile(lambda x: x<12, a)
f = next(k)
print(f)
