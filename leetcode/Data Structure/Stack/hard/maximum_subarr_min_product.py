# https://leetcode.com/problems/maximum-subarray-min-product/

'''
The min-product of an array is equal to the minimum value in the array multiplied by the array's sum.

For example, the array [3,2,5] (minimum value is 2) has a min-product of 2 * (3+2+5) = 2 * 10 = 20.
Given an array of integers nums, return the maximum min-product of any non-empty subarray of nums. 
Since the answer may be large, return it modulo 109 + 7.

Note that the min-product should be maximized before performing the modulo operation. 
Testcases are generated such that the maximum min-product without modulo will fit in a 64-bit signed integer.

A subarray is a contiguous part of an array.
'''

'''
SOLN 
Idea :- Use Monotonic Increasing (non-decreasing) Stack
'''

from typing import List
import itertools as it

def maxSumMinProduct(nums: List[int]) -> int:
    '''
    # O(n)
    Idea :- Monotonic Non-Decreasing Stack to keep start index of Sub-Array
    '''

    # HINT :- consider each element as min-element & try to find the sub-array with that element

    size = len(nums)
    stack = []  # Monotonic Increasing Stack :- holds the tuple(start_idx, min_val)
    #     ie sub-arr := nums[start_idx:];  &  min(sub_arr) := min_val
    res = -1
    prefixSum = list(it.accumulate(nums, initial=0))  # prefixSum[i] = sum(nums[:i])
    def range_sum(s=0, e=size):   
        ''' [s, e) => sum(nums[:i]) '''
        return prefixSum[e] - prefixSum[s]  
    
    for i in range(size):
        v = nums[i]    # {v} need to be insert in Stack
        next_start = i  # next start index to be add on the stack := leftmost_idx s.t. {v} > {leftmost_idx}
        # 1. Till Stack Invariant Satisfy
        while stack and stack[-1][1] > v:
            start_idx, min_val  = stack.pop()

            # try to check for sub-arr
            #   sub_array := nums[start_idx:i]; 
            #   min(sub_array) := min_val        // (due to monotonic increasing nature of stack)
            sum_min_prod = range_sum(start_idx, i) * min_val
            res = max(res, sum_min_prod) 

            next_start = start_idx  # left_most_idx ie < {v}

        # 2. add {next_start} idx on to the stack
        stack.append((next_start, v))

    # Now Stack contains all idx that are start idx of possible sub-arrays 
    # & corresp vals are min-vals of those sub-arrays
    # So lets check each sub-arr candidature
    sum_min_prod = max([range_sum(i)*v for i, v in stack]) # i -> start-idx & v -> min-val
    res = max(res, sum_min_prod)

    return res % (10e8 + 7)  # (10**9) + 7
    

def maxSumMinProduct2(nums):
    ''' 
    O(n)
    Consider each element of nums as min element
    & find corresp window(sub-arr) for such each element
    '''
    size = len(nums)
    prefixSum = list(it.accumulate(nums, initial=0))  # prefixSum[i] = sum(nums[:i])
    def range_sum(s=0, e=size):   
        ''' [s, e) => sum(nums[:i]) '''
        return prefixSum[e] - prefixSum[s]  

    stackl = []  # Monotonically increasing stack/arr in terms of smallest val from left side
    stackr = []  # Monotonically increasing stack/arr in terms of smallest val from right side
    # left boundary (excluding) of subArray for {nums[i]} as min-val 
    left = [0]*size    # at index {i} -> left-most closest small val to nums[i] 
    # right boundary (exlcuding) of subArray for {nums[i]} as min-val
    right = [0]*size   # # at index {i} -> right-most closest small val to nums[i] 

    # O(n)
    # 1. LEFT :- Create left-boundaries of Sub-Array for {nums} at each index
    for i, v in enumerate(nums):  # start from left
        lb = -1  # left boundary for num at {i}
        while stackl:
            if nums[stackl[-1]] < v:
                lb = stackl[-1]
                break 
            stackl.pop()
        left[i] = lb      # track left boundary for sub-arr for index loc {i}
        stackl.append(i) 

    # O(n)
    # 2. RIGHT :- Create right-boundaries of Sub-Array for {nums} at each index
    for i in range(size-1, -1, -1):  # Start from right
        v = nums[i]
        rb = size # right boundary for num at {i}
        while stackr:
            if nums[stackr[-1]] < v:
                rb = stackr[-1]
                break 
            stackr.pop()
        right[i] = rb  # track right boundary of sub-arr for index loc {i}
        stackr.append(i)  # index star from end

    print(left)
    print(right)

    # O(n)
    # 3. calc sum-min-prod
    #    NOTE :- as range_sum() required start param as included & {left} is excluding boundary 
    #            so using {left+1} as it would first element in subArray at moment

    #            sub_arr := nums[s+1:e  ]
    #            minval := num at current interation
    sum_min_prod = [range_sum(s+1, e) * minval for minval, s, e in zip(nums, left, right)] 
    print(sum_min_prod) 
    res = max(sum_min_prod) % (10**9 + 7)

    return res

l = [1,2,3,2]
l = [2,3,3,1,2]

print(maxSumMinProduct2(l))