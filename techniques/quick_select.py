"""
Quick Select
T.C := O(n) in best/avg case
T.C := O(n^2) in worst 

better than Heap Approach

Tip : Use Quick Select if you want to select only 1 or 2 elements 
"""

import random


def partition(arr, left, right):
    """partition array[left:right+1] &
    return location which is holding correct element (as per sorted arr)
    """
    # Select a random pivot index
    pivot_pos = random.randint(left, right)
    pivot = arr[pivot_pos]

    # # Move pivot to the end
    arr[pivot_pos], arr[right] = arr[right], arr[pivot_pos]

    left_tail = left  # position to put element lesser than pivot (ie left side)

    # Move all smaller elements to the left
    for i in range(left, right):
        if arr[i] < pivot:
            # put arr[i] on left side
            arr[left_tail], arr[i] = arr[i], arr[left_tail]
            left_tail += 1
    # Move pivot to its final place
    arr[right], arr[left_tail] = arr[left_tail], arr[right]
    return left_tail


def quickselect(arr, left, right, at_pos):
    """
    Find the correct element at `i` in sorted order of arr

    NOTE: both left & right are inclusive indexes
    """
    if left == right:  # If the list contains only one element
        return arr[left]

    # Find the position
    idx = partition(arr, left, right)

    # The pivot is in its final sorted position
    if at_pos == idx:
        return arr[idx]
    elif at_pos < idx:
        # Searh in left side
        return quickselect(arr, left, idx - 1, at_pos)
    else:
        # Searh in right side
        return quickselect(arr, idx + 1, right, at_pos)


def find_kth_smallest(arr, k):
    """
    Find the k-th smallest element by using quickselect
    """
    n = len(arr)
    return quickselect(arr, 0, n - 1, k - 1)


def find_kth_largest(arr, k):
    """
    Find the k-th largest element by using quickselect
    """
    n = len(arr)
    # (n - k)-th smallest is the k-th largest
    return quickselect(arr, 0, n - 1, n - k)


# Example usage
arr = [3, 2, 1, 5, 6, 4]
k = 2
large = find_kth_largest(arr, k)
small = find_kth_smallest(arr, k)
print(f"{k}-th largest element is {large}")
print(f"{k}-th smallest element is {small}")
