import itertools as it
import operator as op

l = [[1,2], [1,3], [2,4], [2,5], [3,6], [2,1], [3,1]]

*e, = it.groupby(l, op.itemgetter(0))
print(e)
a = {k: list(map(op.itemgetter(1), v)) for k,v in e}
print(a)
