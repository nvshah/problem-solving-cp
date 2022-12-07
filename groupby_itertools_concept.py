import itertools as it
from functools import cmp_to_key

def cc(a, b):
    if a[1] & b[1]:
        return 0
    return -1

l = [[1, {1,2,3}], [2, {2,20}], [3, {30,34}], [4, {30, 40}]]

r = it.groupby(l, key=cmp_to_key(cc))
for k, v in r:
    # print(k)
    print(list(v))