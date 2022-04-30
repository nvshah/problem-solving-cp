# https://leetcode.com/problems/sliding-window-maximum/

from typing import List
from collections import deque


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    '''
        q_idx :- will keep track of most recent max element (index) traversed by window
                so for each window leftmost element in q_idx is the max element in that window
    '''
    # q_idx is non-increasing
    q_idx = deque() # keep track of most recent maximum element index for current window
    l = r = 0
    size = len(nums)
    ans = []

    while r < size:
        # in worst case it can go till leftmost elem of current window
        while q_idx and (nums[r] > nums[q_idx[-1]]): #as we find new max in current window
            q_idx.pop()

        q_idx.append(r) # add element to q_idxueue

        # remove outdated maximum values from q_idx (ie idx not part of current window)
        if l > q_idx[0]:
            # here leftmost index is no longer part of current window
            # so lets throw away expired max val index
            q_idx.popleft()

        if r+1 >= k:
            # 1st window over so onwards l & r both will take 1 steps
            # and all the onwards step = no of window

            # append the result onwards
            ans.append(nums[q_idx[0]])  # max val for current window = leftmost n in q_idx
            l += 1
        r += 1
    return ans
