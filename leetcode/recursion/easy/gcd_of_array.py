# https://leetcode.com/problems/find-greatest-common-divisor-of-array/

from typing import List

def minmax(lst: List[int]):
    ''' Find the min & max eleemnt from the {lst}
    '''
    minimum = lst[0]
    maximum = lst[0]

    for n in lst[1:]:
        if n > maximum:
            maximum = n
        elif n < minimum:
            minimum = n
    return minimum, maximum

def gcd(a, b):
    ''' calculate the gcd for 2 nums a, b using Euc-Algo
    '''
    # 1. Base case
    if b == 0: return a   
    # 2. Recursive Case
    return gcd(b, a%b)

def findGCD(nums: List[int]) -> int:
    return gcd(*minmax(nums))

def findGCD2(nums: List[int]) -> int:
    s, b = min(nums), max(nums)
    return gcd(s, b)

nums = [2,5,6,9,10]  # 2

nums = [7,5,6,8,3]  # 1

nums = [3,3] # 3
ams = findGCD(nums)   
print(ams)