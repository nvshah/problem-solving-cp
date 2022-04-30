# https://leetcode.com/problems/number-of-1-bits/

def hammingWeight1(n: int) -> int:
    ''' Logic rshift + modulo'''
    ans = 0
    while n:
        ans += n%2
        #n = n // 10 # shift right i.e discard last bit|number
        n >>= 1
    return ans

def hammingWeight2(n: int) -> int:
    '''discarding 1 each time 1 by one & counting'''
    ans = 0
    while n:
        n &= (n-1)
        ans += 1
    return ans

def hammingWeight3(n: int) -> int:
    '''via string cnt'''
    return sum(1 for i in bin(n)[2:] if int(i))

n = int('00000000000000000000000000001011',2)
#n = int('00000000000000000000000010000000', 2)
#n = int('11111111111111111111111111111101', 2)
print(hammingWeight1(n))
print(hammingWeight2(n))
print(hammingWeight3(n))
