# https://leetcode.com/problems/n-th-tribonacci-number/description/

'''
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
'''

def tribonacci(n: int) -> int:
    '''Idea: 1-Dimension DP'''
    
    t = [0, 1, 1]
    if n < 3:
        return t[n]
    
    for i in range(3, n+1):
        t = [t[1], t[2], sum(t)]
    
    return t[2]

        