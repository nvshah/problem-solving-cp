from typing import List


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    m = max(candies)
    return [(m-n) <= extraCandies for n in candies]


print(kidsWithCandies([2, 3, 5, 1, 3], 3))
