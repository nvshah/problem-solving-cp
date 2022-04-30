import itertools as it

s = '123#456#789'
i = iter(s)

def takewhile(l, p):
    ''' return grp of elems that satisfy the predicate for entire seq {l} '''
    t = iter(l) # traverser
    while True:
        *s, = it.takewhile(p, t)
        if not s:
            return 
        yield s

c = 3
def p(s):
    global c
    if not c: return False 
    c -= 1
    return True 

*l, = it.takewhile(p, s)
print(l)
