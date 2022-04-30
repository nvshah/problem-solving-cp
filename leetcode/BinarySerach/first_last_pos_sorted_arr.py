# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


from typing import List

'''
Idea -> just don't stop in Binary Search, once index is found. Be Greedy 😉
'''

def searchRange(nums: List[int], target: int) -> List[int]:
    def bs(arr, target, leftMost=True):
        '''
          s = first-most <= target
          e = last-most >= target
        '''
        s, e = 0, len(arr) - 1
        ans = -1
        while s <= e:
            mid = s + ((e - s) // 2)
            if target > arr[mid]:
                s = mid + 1
            elif target < arr[mid]:
                e = mid - 1
            else:
                ans = mid   # Don't stop here, Just Search More ...
                if leftMost:
                    e = mid - 1
                else:
                    s = mid + 1
        return ans

    left = bs(nums, target, leftMost=True)
    right = bs(nums, target, leftMost=False) if left != -1 else -1
    return [left, right]    


def searchRange(nums: List[int], target: int) -> List[int]:

    def bs(s, e):
        '''
          s = first-most <= target
          e = last-most >= target
        '''
        ans = -1
        while s <= e:
            mid = s + ((e - s) // 2)
            if target > nums[mid]:
                s = mid + 1
            elif target < nums[mid]:
                e = mid - 1
            else:
                ans = mid
                break
        return ans, s, e
            
    #1. Find the index of element if exists
    m, l, r = bs(0, len(nums)-1)

    # Target is not found
    if m == -1:
        return [-1, -1]

    # Now if {target} exists multiple times then also it would be between l & r ie [l,r]
    
    #2. Find the left index
    leftMost = m              # leftMost index of {target}
    s, e = l, m-1
    # search ahead in left side of current till reach the end
    while True:  # search the {target} in [l, m-1]
        ml = bs(s, e)[0]
        if ml == -1: break
        leftMost = ml  # {target} found in left part
        e = ml-1 

    #3. Find the Right index
    rightMost = m              # leftMost index of {target}
    s, e = m+1, r
    # search ahead in right side of current till reach the end
    while True:  # search the {target} in [m+1, r]
        mr = bs(s, e)[0]
        if mr == -1: break
        rightMost = mr  # {target} found in right part
        s = mr+1   

    return [leftMost, rightMost] 

def searchRange2(nums: List[int], target: int) -> List[int]:

    def bs(s, e):
        '''
          s = first-most <= target
          e = last-most >= target
        '''
        ans = -1
        while s <= e:
            mid = s + ((e - s) // 2)
            if target > nums[mid]:
                s = mid + 1
            elif target < nums[mid]:
                e = mid - 1
            else:
                ans = mid
                break
        return ans, s, e
            
    #1. Find the index of element if exists
    m, l, r = bs(0, len(nums)-1)

    # Target is not found
    if m == -1:
        return [-1, -1]

    # Now if {target} exists multiple times then also it would be between l & r ie [l,r]
    
    #2. Find the left index
    leftMost = m              # leftMost index of {target}
    s, e = l, m-1
    # search ahead in left side of current till reach the end
    while True:  # search the {target} in [l, m-1]
        ml = bs(s, e)[0]
        if ml == -1: break
        leftMost = ml  # {target} found in left part
        e = ml-1 

    #3. Find the Right index
    rightMost = m              # leftMost index of {target}
    s, e = m+1, r
    # search ahead in right side of current till reach the end
    while True:  # search the {target} in [m+1, r]
        mr = bs(s, e)[0]
        if mr == -1: break
        rightMost = mr  # {target} found in right part
        s = mr+1   

    return [leftMost, rightMost]   

nums = [5, 7, 7, 8, 8, 10]
target = 8

nums = [5,7,7,8,8,10]
target = 6

nums = []
target = 0

ans = searchRange(nums, target)
print(ans) 
