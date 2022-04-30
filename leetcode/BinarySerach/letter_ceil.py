# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

from typing import List


'''
Idea :- start pointer in binary search can reach upto end only in worst case
'''

# Better 
def nextGreatestLetter(letters: List[str], target: str) -> str:
    l = len(letters)
    s, e = 0, l-1
    while s <= e:
        m = s + ((e - s) // 2)
        if target < letters[m]:
            e = m - 1
        else:
            s = m + 1
    return letters[s % l]  # s % l to make index range in [0...len(arr)]

# Alternative Approach
def nextGreatestLetter2(letters: List[str], target: str) -> str:
    l = len(letters)
    s, e = 0, l-1
    ans = letters[0] # by default ans will be first (i.e circular wrap)
    while s <= e:
        m = s + ((e - s) // 2)
        if target <= letters[m]:
            e = m - 1
        else:
            ans = m
            s = m + 1
    return ans

    