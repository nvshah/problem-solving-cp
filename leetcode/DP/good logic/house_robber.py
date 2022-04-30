# https://leetcode.com/problems/house-robber/
from typing import List

'''
Problem :

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is 
that adjacent houses have security systems connected and 
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.


Idea :- 1 Dimensional DP

The way we will solve is local soln --> to global soln
   \
    assume sliding window expanding per iteration & found solution for that window each time
'''

def rob(nums: List[int]) -> int:
    '''
    DP :- with prev 2 Tracking only

    Recursive Eqn (DP) :-
         \
          -> rob := max(arr[0] + arr[2:], rob[1:])

    '''
    # 2 pointers pointing to prev & prev_to_prev computed(ie cached) soln (ie DP)
    # rob1 -> prev to prev
    # rob2 -> prev
    rob1 = rob2 = 0

    # [rob1, rob2, n, n+1, ...]
    for n in nums:
        amt = max(n+rob1, rob2)
        rob1, rob2 = rob2, amt
    
    return rob2  # at last rob2 will point to last loc & thus indicating max robbery amount for all house


