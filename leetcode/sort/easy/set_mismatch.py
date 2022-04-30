# https://leetcode.com/problems/set-mismatch/

'''
1 -> n so cyclic sort approach
'''

from typing import List

def cyclic_sort(arr):
    '''for given element Make element move to its correct position '''
    i, l = 0, len(arr)
    while i < l:
        correct_idx = arr[i] - 1  # correct idx of current element
        if arr[correct_idx] != arr[i]: 
            # move element to its correct index
            arr[i], arr[correct_idx] = arr[correct_idx], arr[i]  # Swap
        else: # duplicate element i.e correct idx already had element placed correctly
            i += 1

def findErrorNums(nums: List[int]) -> List[int]:
    '''
    missing = index + 1
    duplicate = no. at the missing index
    '''
    cyclic_sort(nums)
    for i, n in enumerate(nums):
        if i+1 != n:
            return [n, i+1]

# Alternative Approach
def findErrorNums2(nums: List[int]) -> List[int]:
    ans = [0,0]

    # find duplicate element 
    for n in nums: 
        n = abs(n)
        c_i = n-1
        if nums[c_i] < 0:  # visited earlier
            # visited earlier this idx so duplicate element for this idx is there
            ans[0] = n
        else:
            nums[c_i] *= -1

    # NOTE : there will be 1 idx that will remains +ve i.e missing element index will remains as +ve
    
    # find correct element
    for i, n in enumerate(nums):
        if n > 0:
            ans[1] = i+1
    
    return ans

    

        



nums = [1,2,2,4]
nums = [1,1]
print(findErrorNums(nums))

