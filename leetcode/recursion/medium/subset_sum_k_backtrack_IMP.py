# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

from typing import List
from itertools import compress

'''
Idea : need to check all possible subset combinations
       & return asa 1 satisfies

'''


def canPartitionKSubsets(nums: List[int], k: int) -> bool:
    total = sum(nums) 
    bin = total / k  # target sum for each subset

    # as {bin} cannot be divided evenly ammong {k} subsets
    if bin % 1 != 0: return False

    size = len(nums)
    choosed = [False]*size  # used to track the element selected for current subsets whilst exploring

    def explore(i, subsetSum, k):
        '''
            explore to divide the {nums} into k subset that sums upto {bin}
            if possible then return True otherwise False

            :param i: current pointer to nums
            :param subsetSum: current sum of subset in exploration
            :param k: subsets yet to be explored

            :return : True or False
        '''
        print(i, subsetSum, k)
        if k == 0:  # no more subset to explore
            return True
        
        if subsetSum > bin:  # subset exceeded the bin size so not possible with this way
            return False
        
        if subsetSum == bin :
            # we have found the 1 subset that sums upto bin-size
            # try to found remaining k-1 subsets  
            #! Note now we need to find for all rest elements except currently chosen one
            # i.e scan array from initial position 0 as well i.e i=0
            return explore(0, 0, k-1)

        for j in range(i, size):
            if not choosed[j]:  # if current element is not chosen
                # EXPLORE ---
                choosed[j] = True  # choose the current element
                subsetSum += nums[j] # add the contribution of current element
                isPossible = explore(j+1, subsetSum, k)

                # DECISION ---
                if isPossible:  # found atleast 1 way to get k subsets
                    return True
                
                # BACKTRACK ---
                subsetSum -= nums[j] # after being explored remove the current element contribution
                choosed[j] = False # revoke the current element & make it available for future if needed with other combinations

        return False
    
    return explore(0, 0, k)

nums = [4,3,2,3,5,2,1]
k = 4
nums = [1,3,6,4]
k = 2
print(canPartitionKSubsets(nums, k))

