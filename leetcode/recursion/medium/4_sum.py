# https://leetcode.com/problems/4sum/
from typing import List 

'''
We need to find quadruple arr s.t. sum of it = target
Constrained by := all the elements of quadruple arr must be from diff indexes of input arr
'''

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    '''
    T.C := O(n^3)
    '''
    #1. sort the arr so that to avoid duplicate searching for quadruple
    nums.sort()

    quad = [] # single quadruple -> each elem here belongs to distinguished inndex of {nums} (ie no 2 elem from same {idx})
    res = []  # array of qudruple

    size = len(nums)

    def kSum(k, start, target):
        '''
        :param k: #elems to pick from {nums}
        :param start: idx to start considering picking from {nums}
        :param target: sum(k-picked-elems) must be = target
        '''
        if k != 2:
            # pick the next element for {quad} from nums[start: size-k+1], 
            # Pick from array except last (k-1) elems (so that we can assure for further pickup min-elems availability)
            for i, e in enumerate(nums[start: size-k+1], start):
                if i > start and e == nums[i-1]:  # except first elem check for duplicacy so as to avoid re-finding
                    continue # explored earlier so skip now

                quad.append(e)  # pick
                kSum(k-1, i+1, target-e) # explore
                quad.pop()

        else:
            # 2 Sum (usual problem) :- Base Case
            l, r = start, size-1
            while l < r:
                total = nums[l] + nums[r]
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    # found a pair (ie l, r)
                    res.append([*quad, nums[l], nums[r]])
                    # check for more possibilities
                    l += 1
                    while l<r and nums[l] == nums[l-1]:  # skip already explore member (ie that gets included in {res})
                        l += 1

    # initiate exploration
    kSum(4, 0, target)
    return res 

nums = [1,0,-1,0,-2,2]
target = 0

ans = fourSum(nums, target)
print(ans)



