from functools import cmp_to_key

w = ["nipun", "ishani", "parth", "riddhi"]

def cmp(idx1, idx2):
    l1, l2 = len(w[idx1]), len(w[idx2])
    if l1 > l2:
        return 1
    if l1 < l2:
        return -1
    if l1 == l2:
        if idx1 > idx2:
            return -1
        else:
            return 1

m = max([0,1,2,3], key= cmp_to_key(cmp)) 
print(m)