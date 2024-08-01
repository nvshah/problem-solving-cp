# https://leetcode.com/problems/continuous-subarray-sum/description/

'''
Idea
As we wanna explore sub-array sum for each possible combination, 
We will try to use prefix-sum as it can help us efficiently

Ask : we want to find subarr sum s.t sum % k == 0

Approach 

now let say array length = n 

we want to check if subarr sum from i+1 to j is obeying or not

So subarray_sum = Pj - Pi

   (Pj - Pi) % k = 0

   (Pj % k) - (Pi % k) = 0
   
   Pj % k = Pi % k

   Pj` = Pi`  // where Pj` = Pj%k & Pi` = Pi % k

Hence for given 2 position i & j, if their (prefix sum % k) matches then the arr[i:j] will be candidate

Logic :- 
 If we have some remainder -> then try to find sub-arr-prefix s.t its summed equal to that remainder
                              & 
                              then we can remove that prefix thus making remainder = 0 & thus being divided by k
'''

from typing import List
from collections import accumulate

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSum = accumulate(nums)
        # remainder for each prefix-sum % k
        remainders = map(lambda x: x % k, prefixSum)

        firstOccurence = {} # As 0 will be first prefix-sum (ie without considering any of the elements)
        for i, rem in enumerate(remainders):
            if rem == 0:
                hasMultiples = i >= 1
                if hasMultiples: 
                    # edge case when possible subarray (start at 0)
                    # nums[:i+1] is divided by k, & there are more than 1 items in consideration
                    return True
                continue
            if rem not in firstOccurence:
                firstOccurence[rem] = i 
            elif i - firstOccurence[rem] >= 2:
                return True 
        return False

'''Better way'''
class Solution2:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        Idea : Prefix Sum Track the remainders for all Prefix
            &
            Then check if any upcoming prefix also lead to same remainder thus hinting the
            presence of sub-prefix being multiple of {k}
        '''

        # remainder -> index  // ie remainder belong to prefix till {index}
        prefixRemainder = {0:-1}  # 0->-1 is to avoid 2 zeros found at first
        total = 0
        for i, num in enumerate(nums):
            total += num   # prefix_sum := sum(nums[:i+1])
            r = total % k  # remainder
            if r not in prefixRemainder:  # unique remainder for prefix nums[:i+1]
                prefixRemainder[r] = i    # prefix till {i}
            elif i - prefixRemainder[r] >= 2:  # gap between curr index {i} & prev prefix index is more tha 2 thus sub-arr exists
                return True
        return False
        
            

              