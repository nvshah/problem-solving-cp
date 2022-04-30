# https://leetcode.com/problems/single-element-in-a-sorted-array/

from typing import List


def singleNonDuplicate(nums: List[int]) -> int:
    l = len(nums) 
    if l == 1:
        return nums[0]
    if nums[0] != nums[1]:
        return nums[0]
    if nums[-1] != nums[-2]:
        return nums[-1]
    s, e = 1, len(nums)-2
    while s <= e:
        m = s + (e - s)//2
        print(s, e, m)
        if m % 2 == 0: # even
            if nums[m] == nums[m+1]:  # Look at Left Side
                s = m+1               # Proceed in Right Side
            elif nums[m-1] == nums[m]: # Look at Right Side
                e = m-1                # Proceed in Left Side
            else:
                return nums[m] 
        else: # odd
            if nums[m+1] == nums[m]:  # Look at Right Side
                e = m-1               # Proceed in Left Side
            elif nums[m-1] == nums[m]: # Look at Left Side
                s = m+1               # Proceed in Right Side
            else:
                return nums[m] 

'''
Logic ->

Let O - odd, E - even
Array would be like in this pattern :-

E-O-E-O... {single element} O-E-O-E...

NOTE -> {single element} will always be at even index

Answer will be first pair of E-O where elem(E) != elem(O)

Approach :-

Binary Search Where for given idx check

if it's following E-O-E-O pattern, then need to check in second half
otherwise if O-E-O-E then need to check first half
'''

def singleNonDuplicate2(nums: List[int]) -> int:
    s, e = 0, len(nums)-1
    while s < e:  # till 2 elements are left
        m = s + (e - s)//2
        if m % 2 != 0:
            m = m-1  # Go 1 step back to even idx
        if nums[m] == nums[m+1]:       # As left series is E-O-E-O
            # search in right part
            s = m+2     # skipping the same element
        else:       # even != odd so m can be potential answer (if it's not a part of 2nd half)
            #e = m  # discard right part as right part series is O-E-O-E
            return nums[m]
    return nums[s]
        

            

nums = [1,1,2,3,3,4,4,8,8]
#nums = [3,3,7,7,10,11,11]
#nums = [7,7,10,11,11,12,12]

print(singleNonDuplicate2(nums))

