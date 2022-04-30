# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

from typing import List

def replaceElements(arr: List[int]) -> List[int]:
    # Idea :- iterate from Right -> left (this way val will be memoized according to need)
    rightMax = -1
    for i in range(len(arr)-1, -1, -1):
        arr[i], rightMax = rightMax, max(arr[i], rightMax)  # prevRightMax, nextRightMax
    return arr

arr = [17,18,5,4,6,1]  # [18,6,6,6,1,-1]

arr = [400]  # [-1]
ans = replaceElements(arr)

print(ans)