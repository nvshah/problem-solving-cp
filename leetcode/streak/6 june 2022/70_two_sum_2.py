# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    # d = dict()
    # for i, n in enumerate(numbers):
    #     diff = target - n 
    #     if diff <= n:
    #         if diff in d:
    #             return [d[diff]+1, i+1]
    #     d[n] = i
        
    naruto, sasuke = 0, len(numbers)-1
    while naruto <= sasuke:
        l, r = numbers[naruto], numbers[sasuke]
        chakura = l + r
        if chakura == target:
            return [naruto+1, sasuke+1]
        if chakura < target: # need to add more chakura so naruto step forwards
            naruto += 1
        else :  # need to release some chakura so sasuke step backwards
            sasuke -= 1