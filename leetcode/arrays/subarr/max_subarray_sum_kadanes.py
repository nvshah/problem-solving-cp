# https://leetcode.com/problems/maximum-subarray/

from typing import List


def maxSubArray_ka(nums: List[int]) -> int:
    """*** IMP
    Logic -> Kadane's Algorithm
    gist : start linear traverse from first element, & keep track of
           {current sum, max sum, start idx & end idx of subarray}
           If for any item, item > current sum(i.e including that item)
              then just reset ptrs for subarray from this item.
    """
    curr_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        curr_sum = max(curr_sum + n, n)
        max_sum = max(max_sum, curr_sum)
    return max_sum


def maxSubArray(nums: List[int]) -> int:
    """
    Logic -> Kadane's Algorithm
    """
    maxSum = nums[0]
    currSum = 0
    for n in nums:
        if currSum < 0:
            currSum = 0
        currSum += n
        maxSum = max(currSum, maxSum)
    return maxSum


def maxSubArray2(nums: List[int]) -> int:
    """
    Logic -> Kadane's Algorithm
    gist : start linear traverse from first element, & keep track of
           {current sum, max sum, start idx & end idx of subarray}
           If for any item, item > current sum(i.e including that item)
              then just reset ptrs for subarray from this item.
    """
    ptr1 = 0
    ptr2 = 0
    curr_sum = nums[0]
    max_sum = nums[0]
    for i, n in enumerate(nums[1:], 1):
        curr_sum += n
        if curr_sum < n:
            ptr1 = ptr2 = i
            curr_sum = max_sum = n
        elif curr_sum > max_sum:
            max_sum = curr_sum
            ptr2 = i

    return (nums[ptr1 : ptr2 + 1], max_sum)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# ans = maxSubArray(nums)

sub_arr, m = maxSubArray2(nums)

print(sub_arr, m)
