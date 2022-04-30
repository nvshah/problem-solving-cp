# https://leetcode.com/problems/squares-of-a-sorted-array/

from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    '''
     => 2 pointers method (alike Quick Sort Logic i.e start from left & right)
        ramesh starts from left side & 
        suresh starts from right end
    '''
    l = len(nums)
    ans = [0] * l
    # make all numbers positive (inplace)
    # for i in range(l):
    #     if nums[i] < 0:
    #         nums[i] = -nums[i]
    #     else:
    #         break
    ramesh, suresh = 0, l-1
    # As we know actual number of iterations so using for loop
    for i in range(l-1, -1, -1):  
        nr, ns =  nums[ramesh], nums[suresh]
        if abs(nr) > ns:
            ans[i] = nr**2
            ramesh += 1    # ramesh found answer
        else:
            ans[i] = ns**2
            suresh -= 1   # suresh found answer
    return ans

l = [-6, -4, 1, 2, 3, 5]
a = sortedSquares(l)

print(a)