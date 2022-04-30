# https://leetcode.com/problems/split-array-largest-sum/

from typing import List


def get_chunks_count(arr, thresold):
	'''
	:param arr: -> array to partition into small n chunks
	:param thresold: -> sum of individual chunk cannot go par thresold (i.e <= thresold)
	:return :-> chunks count (i.e n)
	'''
	total = 0  # curr chunk sum
	cnt = 1  # entire array as 1 chunk (atleast)
	for num in arr:
		if total + num > thresold:
			cnt += 1  # num cannot be added into current chunk, so create new chunk
			total = num
		else:
			total += num  # num as a part of current chunk
	return cnt


def splitArray(nums: List[int], m: int) -> int:
    # lowest ans possible = when split array with chunk having only 1 member
    # highest ans possible  = array itself (i.e when no split)
    low, high = max(nums), sum(nums)

    while low < high:  # low = high -> candidate
        candidate = low + (high - low) // 2
        chunks = get_chunks_count(nums, candidate)
        if chunks > m:
            # i.e more chunks than expected so candidate must be higher
            low = candidate + 1
        elif chunks < m:
            # i.e less chunks than expected so candidate may be smaller
            high = candidate - 1
        else:
            # chunks are satisfied so lets look for smaller val of candidate if possible
            high = candidate
    return low


if __name__ == '__main__':
    nums = [7, 2, 5, 10, 8]
    #nums = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
    m = 2

    ans = splitArray(nums, m)

    print(ans)

    #10 17 11 9
