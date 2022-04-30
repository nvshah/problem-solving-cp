# https://leetcode.com/problems/kth-missing-positive-number/

from typing import List
import itertools as it


def findKthPositive(arr: List[int], k: int) -> int:
    s, e= arr[0], arr[-1]
    
    if k < s: # ans is not present in array interval but on LHS
        return k 
    
    l = len(arr)
    capacity = e - s + 1  # capacity of array
    empty_slots = capacity - l  # total missing value in array

    slot_o = k - s + 1  # slot offset i.e to look from all available empty slots in interval (i.e discard LHS values count) 

    if slot_o > empty_slots:  # ans is not present in array interval but on RHS
        offset = slot_o - empty_slots
        return e + offset 

    for i in range(l-1):
        if arr[i] != arr[i+1]:
            available = arr[i+1] - arr[i] -1
            if slot_o <= available:
                # step ahead & find proper position
                return arr[i] + slot_o 
            else:
                # consume all
                slot_o -= available

'''
Using Binary search
Logic :- in natural series i.e [1, 2, 3, 4, ...]
                    indices    [0, 1, 2, 3, ...]

                    So diff    [1, 1, 1, 1, ...]
             missing before    [0, 0, 0, 0, ...]  // -1 on entiere diff vector

            So  num_at_index - index - 1 => number missing before this number

            NICE EXPLANATION )
            --------------- 
    
                formula -> total spaces avail before - filled spaces

                total spaces avail before = element - 1
                filled spaces = index_of_element

                    element - 1 => assume all are missing except current element
                    index       => # element before current element 

                So actual missing = element - 1 - index

    Approach We will check if at any given index in array

      if # of missing is <= k :- search in Left part
      otherwise               :- search in right part


   NOTE := through binary search we will found the most promosing number around which ans will lie
           i.e we can use its index as base index for offset
         
                    
'''

'''
Using Binary search

formula ->total spaces avail before - filled spaces

total spaces avail before = element - 1
filled spaces = index_of_element

So actual missing = element - 1 - index

Approach :-

with above logic we need to find the base index from where we can add offset k
i.e minimum index that is eligible for k offset

Through Binary Search we will found most promisable element around which ans (i.e kth missing element) will lie i.e
So we can use its index as base index for offset k

so add just k to index found via binary seach

Inorder to add k to base idx k > baseidx must satisfy

'''


def findKthPositive_bs(arr: List[int], k: int) -> int:
    l = len(arr)
    if arr[-1] - l == 0:  # no missing in array # edge case 
        return arr[-1] + k 
    s, e = 0, l - 1
    while s <= e:
        m = s + (e-s)//2
        missing_before = arr[m] - 1 - m
        if k <= missing_before:
            e = m - 1
        else:
            s = m + 1
    return s + k      # Here k > s

arr = [2,3,4,7,11]
k = 5

# arr = [1,2,3,4]
# k = 2

# arr = [5,6,7,8,9]
# k = 9

ans = findKthPositive_bs(arr, k)
print(ans)


    
