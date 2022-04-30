# https://leetcode.com/problems/can-place-flowers/

from typing import List


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool: 
    fb = [0, *flowerbed, 0]  # appending 0 so to cover egde cases of 3 odd logic

    left = n

    for i in range(1, len(flowerbed)+1):
        if not left:
            return True
        # look at left & right for each flowers i.e 0, 0, 0
        if not (fb[i] or fb[i-1] or fb[i+1]):
            # ie 0 0 0 so we can place flowers
            fb[i], left = 1, left - 1
    return not left

def canPlaceFlowers2(flowerbed: List[int], n: int) -> bool: 
    # if first is not full then we need to assume empty pot ahead of it
    # so that we can have our 3 consecutive pot assumption work all over
    empty_in_seq = not flowerbed[0]
    left = n
    print(left)
    for f in flowerbed:
        if left <= 0:
            return True
        if f:
            # flower is present
            # Try to place the flower in previous Empty Places
            # formula to calculate no. of flower can be put given n consecutive empty spaces
            left -= int((empty_in_seq - 1 )/ 2)  # int division rounds towards 0
            empty_in_seq = 0 # reset as the flower is found in between
        else:
            empty_in_seq += 1
    
    # Edge case for Last Position flower
    # formula to calculate no. of flower can be put at last pos 
    left -= (empty_in_seq // 2)

    return left <= 0
flowerbed = [1,0,0,0,1]
n = 1
flowerbed = [1,0,0,0,1]
n = 1
canPlace = canPlaceFlowers2(flowerbed, n)
print(canPlace)

