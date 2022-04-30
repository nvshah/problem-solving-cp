import itertools as it
from typing import List

def runningSum(nums: List[int]) -> List[int]:
    return it.accumulate(nums)

if __name__ == '__main__':
    print(*runningSum([1,2,3,4]))