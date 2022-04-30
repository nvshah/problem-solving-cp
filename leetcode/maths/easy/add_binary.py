# https://leetcode.com/problems/add-binary/
import itertools as it 

def addBinary(a: str, b: str) -> str:
    res = []  # store the result digits in reverse manner
    carry = 0 # carry during sum

    zero_ord = ord('0')

    # Perform traditional sum from R -> L (ie in reverse manner)
    for da, db in it.zip_longest(a[::-1], b[::-1], fillvalue='0'): 
        digitA = ord(da) - zero_ord
        digitB = ord(db) - zero_ord

        total = digitA + digitB + carry 
        carry, newDigit = divmod(total, 2)
        res.append(str(newDigit))
    
    if carry:
        res.append('1')
    
    return ''.join(reversed(res))

a = '11'
b = '1'
c = addBinary(a, b)
print(c)

