# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/description/
from typing import List 

'''
Running Prefix | Suffix
'''

# O(n) time | O(1) space
def getSumAbsoluteDifferences(nums: List[int]) -> List[int]:
    N = len(nums)
    total = sum(nums)
    left_sum = 0

    res = []

    for i in range(N):
        num = nums[i]
        left_count = i 
        right_count = N - left_count
        left_val =  num*left_count - left_sum

        right_sum = total - left_sum
        right_val = right_sum - num*right_count

        res.append(left_val + right_val)

        left_sum += num 
    
    return res 