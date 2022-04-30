# https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List
from functools import reduce




def lengthOfLIS1(nums: List[int]) -> int:
    '''
     Idea :- DP on same array from Right to left
             As Comparing String of lenght 2 will include the Comparing String of length 1
    '''
    size = len(nums)
    # dp[i] denotes the maximum Length Of Subseq possible for characters from index {i} if i included
    LIS = [1]*size  # LIS

    for i in range(size-2, -1, -1):
        # we can take one by one combination with sub-indexes
        for j in range(i+1, size):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])
            
    return max(LIS)

# def lengthOfLIS(nums: List[int]) -> int:
#     '''
#      Idea :- DP on same array from Right to left
#              As Comparing String of lenght 2 will include the Comparing String of length 1
#     '''
#     size = len(nums)
#     # dp[i] denotes the maximum Length Of Subseq possible for characters from index {i}
#     dp = [1]*size  # LIS

#     for i in range(size-2, -1, -1):
#         # we can take one by one combination with sub-indexes
#         dp[i] = max(1, dp[i+1], *[1+dp[j] for j in range(i+1, size) if nums[i] < nums[j]])
            
#     return dp[0]  # maximal sub-seq from starting

# def lengthOfLIS2(nums: List[int]) -> int:
#     '''
#      Idea :- DP on same array from Right to left
#              As Comparing String of lenght 2 will include the Comparing String of length 1
#     '''
#     return reduce(lambda dp, i: 1 + dp if nums[i] < nums[i+1] else dp, range(len(nums)-2, -1, -1), 1)

nums = [10,9,2,5,3,7,101,18]
#nums = [0,1,0,3,2,3]
#nums = [7,7,7,7,7,7,7]
#print(lengthOfLIS(nums))
nums = [10, 2, 3]
#print(lengthOfLIS2(nums))
print(lengthOfLIS1(nums))

