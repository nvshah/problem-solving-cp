# https://leetcode.com/problems/multiply-strings/
import re

'''
Remember :

When you multiply 2 numbers -> then max length of output will be total sum of digit count
of both the numbers

Normally We compute output in Reverse Order (ie Right to Left)
So consider the indexing of input numbers from R->L side
'''

def simplifyNum(n):  # For Positive num only
    regex = r"[1-9][0-9]*"
    m = re.search(regex, n)
    if m:
        return m.group()
    return "0"


def multiply(num1: str, num2: str) -> str:
    '''
    Traditional Multiplication Method (ie going in Reverse order from Right -> Left)
    '''

    if "0" in [num1, num2]:  # Edge Case  0 * anything = 0
        return "0"  
    
    # We need to traverse 2 num in reverse (ie R->L ) for calculating multiplication
    *rNum1, = map(int, num1[::-1]) # reversed num1 list
    rNum2 = list(map(int, reversed(num2))) # reversed num2 list

    # Thus Eg "123" -> "321"  (where at 0 index : 3, at 1 index : 2 & likewise) 

    size1, size2 = len(num1), len(num2)
    # max digits in ouput := sum of digits of both input numbers
    resSize = size1+size2
    res = [0] * (resSize)
    
    # 1. Compute the Multiplication res traditionally (ie R->L traversal)
    for i1, d1 in enumerate(rNum1):
        for i2, d2 in enumerate(rNum2):
            # pos of curr-resulted digit in output {res} is decided by sum of curr idx of both input numbers
            p = i1 + i2 # position
            res[p] += d1 * d2 
            # now we need to take care of carry & remainder (ie mod 10)
            carry, remain = divmod(res[p], 10)
            res[p] = remain    # make curr position {p} digit in range 0-9
            res[p+1] += carry  # transfer carry to next pos ie {p+1} index in {res} output

    # 2. Actually final result is reversed (as we calculated R->L) but we read from L->R so ... 
    res = res[::-1]

    # 3. Simplify the output result (ie '00120' = '120')
    beg = 0
    while (beg < resSize) and (beg == 0):
        beg += 1
    
    # 4. convert all necessary digits from int -> str
    res = map(str, res[beg:])
    return ''.join(res)

def multiply2(num1: str, num2: str) -> str:
    '''
    Traditional Multiplication Method (ie going in Reverse order from Right -> Left)
    '''

    if "0" in [num1, num2]:  # Edge Case  0 * anything = 0
        return "0"  
    
    # We need to traverse 2 num in reverse (ie R->L ) for calculating multiplication
    *rNum1, = map(int, num1[::-1]) # reversed num1 list
    rNum2 = list(map(int, reversed(num2))) # reversed num2 list

    # Thus Eg "123" -> "321"  (where at 0 index : 3, at 1 index : 2 & likewise) 

    size1, size2 = len(num1), len(num2)
    # max digits in ouput := sum of digits of both input numbers
    resSize = size1+size2
    res = [0] * (resSize)
    
    # 1. Compute the Multiplication res traditionally (ie R->L traversal)
    for i1, d1 in enumerate(rNum1):
        for i2, d2 in enumerate(rNum2):
            # pos of curr-resulted digit in output {res} is decided by sum of curr idx of both input numbers
            p = i1 + i2 # position
            res[p] += d1 * d2 
            # now we need to take care of carry & remainder (ie mod 10)
            carry, remain = divmod(res[p], 10)
            res[p] = remain    # make curr position {p} digit in range 0-9
            res[p+1] += carry  # transfer carry to next pos ie {p+1} index in {res} output

    # 2. Actually final result is reversed (as we calculated R->L) but we read from L->R so ... 
    res = ''.join(map(str, reversed(res)))

    # 3. Simplify the output result (ie '00120' = '120')
    return simplifyNum(res)


num1 = "2"
num2 = "3"

num1 = "123"
num2 = "456"
res = multiply2(num1, num2)
print(res)




