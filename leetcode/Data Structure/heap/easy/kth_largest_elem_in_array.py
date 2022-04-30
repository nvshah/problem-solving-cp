# https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/

from typing import List
import heapq as hp


def findKthLargest1(nums: List[int], k: int) -> int:
    return hp.nlargest(k, nums)[-1]

def findKthLargest2(nums: List[int], k: int) -> int:
    hp.heapify(nums)
    for _ in range(len(nums)-k):
        hp.heappop(nums)
    return nums[0]

def findKthLargest4(nums: List[int], k: int) -> int:
    size = len(nums)
    offset = size - k

    def quick_select(l, r):
        ''' Using lamuto Algorithm '''
        pivot, ptr = nums[r], l 
        for i in range(l,r):
            if nums[i] <= pivot:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        nums[ptr], nums[r] = nums[r], nums[ptr]

        if offset == ptr: return nums[offset]
        if offset < ptr: return quick_select(l, ptr-1)
        else: return quick_select(ptr+1, r)

    return quick_select(0, size-1)

def findKthLargest3(nums: List[int], k: int) -> int:
    '''
        using Quick Sort but using Lamuto Partition
    '''
    size = len(nums)
    offset = size - k

    def partition(s, e):
        if s == e: # as cannot divide the array of size 1
            return s 
        # ptr will point to idx s.t all elem below idx will be <= pivot 
        # so whatever idx ptr point to will be first member i.e greater than pivot
        pivot, ptr = nums[e], s 

        for i in range(s, e):
            if nums[i] <= pivot:
                nums[ptr], nums[i] = nums[i], nums[ptr] # swap
                ptr += 1
        # place pivot to its correct location ie at ptr & pivot stays at e
        nums[ptr], nums[e] = nums[e], nums[ptr]
        return ptr

    def find(s, e):
        pos = partition(s, e)
        if pos == offset:
            return nums[pos]
        elif offset > pos:
            return find(pos+1, e)
        else:
            return find(s, pos-1)

    return find(0, size-1)

def find_kth_largest_via_quick_sort(nums, k):
    '''
        find the kth largest element
    '''
    size = len(nums)

    def partition(s, e):
        if s == e:  # cannot partition single element
            return s

        p = s
        pivot = nums[p]
        p1, p2 = s+1, e

        while True:
            # left search
            while p1 <= p2 and nums[p1] <= pivot:
                p1 += 1 
            # right search
            while p1 <= p2 and nums[p2] >= pivot:
                p2 -= 1

            if p1 > p2:  # partition done
                break

            if p1 < p2:
                # swap the left & right vals
                nums[p1], nums[p2] = nums[p2], nums[p1]

            p1, p2 = p1+1, p2-1

        # swap the pivot (misnomer) to its correct location
        nums[p2], nums[p] = nums[p], nums[p2]

        return p2  # position of pivot

    def find(s, e, k):
        print(s, e, k)
        p = -1  # initially we dont know which index will be correct
        while s <= e:
            p = partition(s, e)
            print('pivot', p, nums)
            offset = size-p  # offset from right end (largest end)
            if k == offset:
                return nums[-k]
            elif k < offset:
                # search in right part
                s = p+1
            else:
                # search in left part
                e = p-1

        return None
    
    return find(0, size-1, k)

nums = [3,2,1,5,6,4]
k = 3

#ans = find_kth_largest_via_quick_sort(nums, k)
ans = findKthLargest2(nums, k)
print(nums)
print(ans)