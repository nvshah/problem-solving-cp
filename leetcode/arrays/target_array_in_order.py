from typing import List

# Que -> https://leetcode.com/problems/create-target-array-in-the-given-order/


def createTargetArray(nums: List[int], index: List[int]) -> List[int]:
    target = []
    for i in range(len(nums)):
        target.insert(index[i], nums[i])
    return target


nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]

nums = [1, 2, 3, 4, 0]
index = [0, 1, 2, 3, 0]

nums = [1]
index = [0]


ans = createTargetArray(nums, index)

print(ans)
