# https://leetcode.com/problems/number-of-1-bits/

def hammingWeight(n: int) -> int:
    '''via string cnt'''
    return sum(1 for i in bin(n)[2:] if int(i)) 