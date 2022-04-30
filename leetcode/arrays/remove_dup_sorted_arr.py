from typing import List


def removeDuplicates(nums: List[int]) -> int:
    l = len(nums)
    if l < 1:
        return
    start = 0
    lead = 1

    while lead < l-1:
        while nums[start] == nums[lead]:
            if lead == l:
                break
            lead += 1
        else:
            start += 1
            lead += 1
            nums[start], nums[lead] = nums[lead], nums[start]
            continue

    return start+1

def removeDuplicates(nums: List[int]) -> int:
    l = 0 
    for r in range(len(nums)):
        if nums[r] != nums[l]:
            l += 1
            nums[l] = nums[r]
    return l+1

def removeDuplicates3(nums: List[int]) -> int:
    l = 1 # pos where to place next unique element 
    for r in range(1, len(nums)):
        if nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l += 1  # next pos to place next unique element
    return l+1


if __name__ == '__main__':
    pass
