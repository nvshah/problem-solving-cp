from typing import List

def binary_search(arr, t, s=0, e=-1):
    ''' Binary Search for Sorted Array using Iterator Approach '''
    while s <= e:
        m = s + ((e - s) // 2)
        if t > arr[m]:
            s = m + 1
        elif t < arr[m]:
            e = m - 1
        else:
            return m
    return -1

def find_avalanche(nums: List[int]) -> int:
    """
    nums is array (with distinct values)
    Find the index of maximum number if array is rotated atleast
    NOTE - pivot is largest elem because there can be only chance that
           largest elem,the following element will always be smallest
    (Assuming Unique elements in array)
    :param nums: list of rotated sorted array
    :return: index of maximum number if array is rotated (i.e except first & last element index)
    """
    s, e = 0, len(nums) - 1
    while s <= e:
        m = s + (e - s) // 2
        if m < e and nums[m] > nums[m + 1]:
            return m  # pivot found i.e Peak to-> smallest
        elif m > s and nums[m - 1] > nums[m]:
            return m - 1  # pivot found i.e Peak to-> smallest
        elif nums[s] < nums[m]:
            # increasing left part so max element will lie in right part
            s = m + 1
        else:
            # peak can be in left part (as all elem in right part is smaller than left part)
            e = m - 1
    return -1


def search(nums: List[int], target: int) -> int:
    p = find_avalanche(nums)
    if p == -1:
        # No rotation on nums so do normal binary search on entire array
        return binary_search(nums, target)
    # we've found 2 sorted array
    elif nums[p] == target:
        return p
    elif target < nums[0]:
        # search in right part of p (i.e lower values bunch)
        return binary_search(nums, target, p + 1, len(nums)-1)
    else:
        # search in left part of p (i.e higher values bunch)
        return binary_search(nums, target, 0, p-1)

def search(nums: List[int], target: int) -> int:
    '''
    idea :- rotated sorted array contain 2 parts : 
            1) Left sorted part
            2) Right sorted part
            &
            All the elements in Left Sorted Part are greater than Right Sorted Part
            
            Note :- Either part can be empty as well 
                    Eg nums = [1,2,3]
                        nums = [3,2,1]
    '''
    l, r = 0, len(nums)-1
    
    while l <= r:
        m = (l + r) // 2
        v = nums[m]
        
        if target == v:
            return m
        
        if nums[l] <= v:        # {m} lies in Left Sorted Part
            if nums[l] <= target < v: # {target} may resides in left sorted part
                r = m-1
            else:                     # {target} may resides in right sorted part
                l = m+1
        else:                   # {m} lies in Right Sorted Part  
            if v < target <= nums[r]: # {target} may resides in right sorted part
                l = m+1
            else:          
                r = m-1               # {target} may resides in left sorted part
    return -1

if __name__ == '__main__':
    arr = [4,5,6,1,2,3]
    #arr = [2,2,2,2,2,9,2]
    #pivot = find_pivot_in_rotated_sorted_array_with_duplicates(arr)
    #ans = search_in_rotated_sorted_array(arr, 1)

    idx = search(arr, 5)

    print(idx)