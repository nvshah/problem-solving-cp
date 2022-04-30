# https://leetcode.com/problems/find-all-duplicates-in-an-array/

from typing import List


def findDuplicates(nums: List[int]) -> List[int]:
    '''Cyclic Sort '''
    i, l = 0, len(nums)
    while i < l:
        c_i = nums[i]-1
        if nums[c_i] != nums[i]:  # element is at wrong index
            nums[i], nums[c_i] = nums[c_i], nums[i]
        else:
            i += 1
    ans = [nums[i] for i in range(l) if nums[i] != i + 1]
    return ans

nums = [4,3,2,7,8,2,3,1]
nums = [1,1,2]
nums = [1]
print(findDuplicates(nums))
