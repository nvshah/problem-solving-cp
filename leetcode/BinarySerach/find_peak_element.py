# https://leetcode.com/problems/find-peak-element/


from typing import List


# Bitonic Array  [-> e <-]
def findPeakElement(nums: List[int]) -> int:
    s, e = 0, len(nums)-1
    while s != e:
        m = s + (e-s)//2
        if nums[m] > nums[m+1]:
            # search in left part (i.e m can be a candidate for peak val)
            e = m
        else:
            # search in right part (i.e m+1 can be a candidate for peak val)
            s = m+1
    return e


nums = [1, 2, 3, 1]

ans = findPeakElement(nums)

print(ans)
