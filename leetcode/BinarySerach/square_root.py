# https://leetcode.com/problems/sqrtx/

# ref https://blogs.sas.com/content/iml/2016/05/16/babylonian-square-roots.html

'''
  BABYLONIAN LOGIC :- 
  ref https://blogs.sas.com/content/iml/2016/05/16/babylonian-square-roots.html

  intital values :- 
    {2, 7, 20, 70, 200, 700 }


  NOTE this is similar to math.isqrt() in python
    import math
    print(math.isqrt(10)) # 3
'''

from math import trunc, floor

def find_floor(arr, t):
    '''return the index of element (assuming index start from 1)'''
    s, e = 0, len(arr)-1
    while s <= e:
        m = s + (e - s) //2
        if t > arr[m]:
            s = m + 1
        elif t < arr[m]:
            e = m - 1
        else:
            return m + 1
    return e + 1

def speculate_initial_val(n):
    # find the initial val
    zeros = pow(10, len(str(n)) // 2)
    l, u = 2 * zeros, 7 * zeros
    l_sq, u_sq = 4 * zeros, 49 * zeros
    m = l_sq + (u_sq - l_sq) // 2  # closeness|proximity decision
    i = l if n < m else u    # initial val
    return i

def babylonian_sqrt(num):
    '''
    Find the isqrt via babyleon method of approximation
    '''
    if num < 225:
        sqs = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]
        return find_floor(sqs, num)
    i = speculate_initial_val(num) 
    print('Initial : ', i)
    while True:
        #b = round((i + num / i) / 2, decimal_precision)
        #b = floor((i + num / i) / 2)
        b = (i + num / i) / 2
        print('-> ', b)
        if floor(i) == floor(b):
            break
        else:
            i = b
    return floor(i)

def isqrt(n):
    '''
    math.isqrt() via Binary Search
        Logic ->

    Let's consider
    number - n, divisor - d

    if d divides n into exact d parts then we can say that d is exact square root of n
    if d divides n into more than d parts so -> need to lower the divider
    if d divides n into less than d parts sp -> need to increase the divider
    '''
    s, e = 1, n
    while s <= e:
        m = s + (e-s) // 2
        q = n // m
        if m == q: 
            # d
            # m divides x into exact m parts, i.e found exact square root
            return m
        elif q > m:
            # m divides x into more than m parts, i.e more parts than expected so increase the divider
            s = m+1
        else:
            # m divides x into less than m parts i.e less parts than expected so decrease the divider
            e = m-1
    return e

def mySqrt(x: int) -> int:
    # return babylonian_sqrt(x)
    return isqrt(x)


if __name__ == '__main__':
    S = 2147395599
    #i = 70
    ans = mySqrt(S)
    print('Answer : ', ans)
