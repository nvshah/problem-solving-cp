# https://www.lintcode.com/problem/659/

import itertools as it

''' SYSTEM DESIGN 

QUE

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode


'''

def takewhile(p, l):
    ''' return grp of elems that satisfy the predicate for entire seq {l} '''
    t = iter(l) # traverser
    while True:
        *s, = it.takewhile(p, t)
        if not s:
            return 
        yield s


"""
@param: strs: a list of strings
@return: encodes a list of strings to a single string.
"""
def encode(strs):
    # str-length + '#' + str   // for each string txt
    return ''.join(f'{len(s)}#{s}' for s in strs)


"""
@param: str: A string
@return: dcodes a single string to a list of strings
"""
def decode(str):
    res = []
    t = iter(str)
    while True:
        # find individual part (ie Single Word)
        *s, = it.takewhile(lambda x: x!='#', t)
        if not s: break
        # decode individual part (ie Single Word)
        l = int(''.join(s))  # find the length of word
        g = it.islice(t, l)  # get the word
        r = ''.join(g)       
        res.append(r)       # record word in result
        
    return res 

i = ["lint","code","love","you"]

e = encode(i)
print(e)
d = decode(e)
print(d)