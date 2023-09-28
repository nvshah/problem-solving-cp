from typing import List
import itertools as it

# Que -> https://leetcode.com/problems/shuffle-the-array/

# O(n) time, O(1) space
def shuffle(nums: List[int], n: int) -> List[int]:
    '''Encode-Decode - BITS Manipulation (INPLACE) 
    
    => BIT manipulation is faster than arithmetic
    
    IDEA: As num can be max 1000 (Constraint)
    generally int take 32 bit but as we have max 1000 val in nums, 
    & 1000 val can be stored only in 10 bit so ideally we can store
    2 nums (20 bit) in 1 number (32 bit)  // ENCODING
    & 
    then DECODE it back to get 2 numbers from that encoded 20 bit number in single 32 bit number
    '''

    # ENCODE
    for i in range(nums):
        nums[i] = nums[i] << 10 # shift x by 10 bit left, making room for y
        nums[i] = nums[i] | nums[i + n] # store x & y together in same spot in memory (ie place y in space created above)
    
    MAX_VAL_FOR_10_BITS = 2**10 - 1 # formula (2^n-1) for max value in n bit space
    j = 2*n-1 # last index, to fill values from last (ie Right to Left)

    # DECODE
    for i in range(n-1, -1, -1): # first half in reverse order
        y = nums[i] & MAX_VAL_FOR_10_BITS # Extract last 10 bit from RHS
        x = nums[i] >> 10 # shift x by 10 right, removing space created for y

        nums[j], nums[j-1] = y, x
        j -= 2 # filled spots
    
    return nums
    
# O(n) time | O(n) space
def shuffle1(nums: List[int], n: int) -> List[int]:
    res = []
    for i in range(n):
        res.append(nums[i])
        res.append(nums[i+n])
    return res

# O(n) time | O(n) space
def shuffle2(nums, n):
    # Faster
    return it.chain.from_iterable(zip(nums[:n], nums[n:]))


a1 = shuffle([2, 5, 1, 3, 4, 7], 3)
a2 = shuffle2([2, 5, 1, 3, 4, 7], 3)

print(a1)
print(*a2)
