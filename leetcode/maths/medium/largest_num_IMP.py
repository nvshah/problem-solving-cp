# https://leetcode.com/problems/largest-number/
from functools import cmp_to_key
from typing import List

'''
QUE
Given a list of non-negative integers nums, 
arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

'''

def largestNumber(nums: List[int]) -> str:
    '''
    Idea :- Largest Number should be on MSB side
            
            This is Generalization of base case cmp (ie with 2 Nums only)
    '''
    *nums, = map(str, nums) # str repr

    def mycmp(n1, n2):
        '''
        cmp 2 num based on total ordering & returns either {1, -1, 0}
        -1 := n1
        1 := n2
        '''
        # Eg n1 = '3' & n2 = '30' then 2 choices :- '330' & '303' => '330' is picked
        if n1 + n2 > n2 + n1:
            return -1 # pick n1 first
        else:
            return 1 # pick n2 first
        
    nums.sort(key=cmp_to_key(mycmp))  # place number accordingly on Left Side
    return str(int(''.join(nums)))



