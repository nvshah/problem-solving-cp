# https://leetcode.com/problems/find-k-closest-elements/

from typing import List


def findClosestElements1(arr: List[int], k: int, x: int) -> List[int]:
    n = len(arr)      # size
    if k == n: return arr  # Edge Case 
    lo, hi = 0, n-1  
    
    # 1. Binary Search
    while lo <= hi: 
        mi = (lo + hi) // 2
        if arr[mi] == x:
            l, r = mi-1, mi+1
            break 
        if arr[mi] > x:  # Search in Left
            hi = mi - 1
        else:
            lo = mi + 1
    else:
        l, r = hi, lo

    # 2 ptr method to find closest nums
    while 0 <= l < r < n:     
        # Elements Found = element lying between (l, r) // excluding l & r
        dl = abs(arr[l] - x)
        dr = abs(arr[r] - x)
        if dl <= dr:
            l -= 1
        elif dl > dr:
            r += 1
        if r - l - 1 == k:    # k closest elements found
            return arr[l+1:r]
            
    if l == -1:   
        return arr[:k]  # first k elements
    if r == n:
        return arr[-k:] # last k elements

def findClosestElements2(arr: List[int], k: int, x: int) -> List[int]:
    ''' IDea : Lamuto Quick Sort Pivot Find Logic '''
    l, r = 0, len(arr)-1

    while (r - l + 1) != k:
        dl = abs(arr[l] - x)
        dr = abs(arr[r] - x)

        if dl <= dr:
            r -= 1
        else:
            l += 1
        
    return arr[l:r+1]

def findClosestElements3(arr: List[int], k: int, x: int) -> List[int]:
    ''' IDea : Find Window via Binary Search '''
    # mid val will point the start of window & window needs length = k so hi is last kth elem
    lo, hi = 0, len(arr)-k

    # Here in Binary Search it will always converge entirely ie log(n)
    # Thus we want lo & hi to point to same num at the end of this binary search & that number will be start index of (ideal) window
    while lo < hi:
        mi = (lo + hi) // 2  
        # e is the next element outside the window (on right side)
        s, e = mi, mi+k     # start & end of window (start including)
        if x - arr[s] > arr[e] - x:
            # {s} is not closest compare to {e}
            # so include {e} in window & exclude {s}  
            # thus excluding all left side of curr window [s, e)  ie all elem <= {s}
            lo = mi + 1
        else:
            # {mi} can be equally or less closest  
            # thus neglecting all right side of current window [s, e)  ie all elem >= {e}
            hi = mi
    
    # Now lo = hi & thus this will be start idx of window
    return arr[lo: lo+k]
    
arr = [1,2,3,4,5]
k = 4
x = -1

arr = [1,1,1,10,10,10]
k = 1
x = 9

arr = [-2,-1,1,2,3,4,5]
k = 7
x = 3
ans = findClosestElements2(arr, k, x)
print(ans)