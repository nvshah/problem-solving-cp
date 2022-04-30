# https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/
from typing import List
from itertools import islice
import heapq as hq

'''
QUE
You are given a 0-indexed array nums of distinct integers. You want to rearrange the elements in the array such that every element in the rearranged array is not equal to the average of its neighbors.

More formally, the rearranged array should have the property such that for every i in the range 1 <= i < nums.length - 1, (nums[i-1] + nums[i+1]) / 2 is not equal to nums[i].

Return any rearrangement of nums that meets the requirements.
'''

'''
Approach 1 :- Sorting + Greedy
T.C := O(n*logn)
'''
def rearrangeArray1(nums: List[int]) -> List[int]:
    l = len(nums)
    # 1. sort (inorder to get larger & smaller half)
    nums.sort()
    res = [0]*l
    
    u = l - (l // 2)  # upper bound of first half
    
    # 2. Fill all Odd Places in {res} (ie from first half of sorted array)
    f = zip(range(0, l, 2), islice(nums, u))  # First Half with resp pos in {res}
    for i, n in f:
        res[i] = n
    
    # 2. Fill all Even Places in {res} (ie from Second half of sorted array)
    s = zip(range(1, l, 2), islice(nums, u, l))  # Second Half with resp pos in {res}
    for i, n in s:
        res[i] = n

    return res

'''
[****] Better Approach
-------
Approach 1 :- Heap (Half Sort) + Greedy
T.C := O(n*logn)
'''
def rearrangeArray2(nums: List[int]) -> List[int]:
    l = len(nums)
    res = [0]*l

    # 1. sort (inorder to get larger & smaller half)
    hq.heapify(nums)
    
    # 2. Fill all Odd Places in {res} from heap (ie u smallest val))
    for i in range(0, l, 2) :  # First Half
        res[i] = hq.heappop(nums)
    
    # 2. Fill all Even Places in {res} from Array (ie u largest val remaining in array)
    for i, n in zip(range(1, l, 2), nums): # Second Half
        res[i] = n

    return res

nums = [1,2,3,4,5]  # [1, 4, 2, 5, 3]

nums = [6,2,0,9,7]  # [0, 7, 2, 9, 6]
ans = rearrangeArray2(nums)
print(ans)

    
        


