# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

# O(1) time | O(1) space
def countOdds(low: int, high: int) -> int:
    size = high - low + 1
    count = size // 2

    # length is odd & start is also odd
    if size % 2 and low % 2:
        count += 1

    return count