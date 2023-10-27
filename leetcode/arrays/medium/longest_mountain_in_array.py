# https://leetcode.com/problems/longest-mountain-in-array/

from typing import List

def longestMountain2(arr: List[int]) -> int:
    '''Expand & Search'''
    if len(arr) < 3: return 0
    res = 0
    i = 1
    while i < len(arr)-1: # till penultimate point
        isPeak = arr[i-1] < arr[i] > arr[i+1]
        if not isPeak:
            i += 1
            continue
        # find the boundaries of this peak
        l = i-2
        while l >= 0 and arr[l] < arr[l+1]: # expand to left
            l -= 1
        r = i+2
        while r < len(arr) and arr[r] < arr[r-1]: # expand to right
            r += 1
        res = max(res, r-l-1)  # (l,r) are excluding indexes

        i = r # jump to next mountain search

    return res

def longestMountain1(arr: List[int]) -> int:
    '''3 Pointers '''
    if len(arr) < 3: return 0
    # l: start, m: top, r: end of mountain [l->m<-r]
    l = m = r = 0
    res = 0

    while r < len(arr)-1: # till penultimate point
        if arr[r] > arr[r+1]: # decreasing
            if l == r:
                l = r = m = r+1 # move all as this is not a mountain
            else:
                r += 1  # move [r] away from [m]
        elif arr[r] == arr[r+1]: # flat 
            if m != r:
                res = max(res, r-l+1) # account previous mountain defined by [l->m<-r]
            m = l = r = r+1 # move all on flat surface
        else: # increasing
            if m != r:
                res = max(res, r-l+1) # account previous mountain defined by [l->m<-r]
                l = r  # [l] helps to track start of next possible mountain
            m = r = r+1 # move [m] & [r] till reach peak
    if m != r: 
        res = max(res, r-l+1)
    return res