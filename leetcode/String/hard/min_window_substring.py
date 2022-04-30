# https://leetcode.com/problems/minimum-window-substring/

from collections import Counter as ctr
from sys import maxsize

def minWindow(s: str, t: str) -> str:
    '''
     Idea :- use left & right pointer to find the ans in O(n)
    '''
    size_t, size_s = len(t), len(s)
    if size_t > size_s: return ''  # edge case 1
    if size_t == size_s: return s if ctr(t) == ctr(s) else '' # edge case 2

    counts_t = ctr(t)
    window = {}
    
    best_window_bounds = (-1, -1)  # optimal window bounds
    #window_size = float("inf")
    best_window_size = maxsize   # optimal window_size

    l = 0 # left pointer
    have = 0  # current fulfillment achieved 
    need = len(counts_t)  # total number of milestone needs to be fulfilled

    for r in range(size_s):
        last = s[r] # last character in current window
        if last in counts_t: # if character {c} is being asked for 
            window[last] = 1 + window.get(last, 0)  # mark the count of {c} in current window
            if window[last] == counts_t[last]:
                # one of the requirement is fulfilled
                have += 1

                while have == need: 
                    # we find the solution
                    curr_window_size = r-l+1
                    if curr_window_size < best_window_size:
                        best_window_size = curr_window_size
                        best_window_bounds = (l, r+1)

                    # Try to reduce the window size from left (to find more optimal solution)
                    first = s[l]  # first character in current window
                    if first in counts_t:
                        window[first] -= 1

                        if window[first] < counts_t[first]: 
                            # if required {first} falls below thresold in current window
                            have -= 1
                    
                    l += 1 # move left ptr 1 step ahead

    return s[slice(*best_window_bounds)]


s = "ADOBECODEBANC"
t = "ABC"

s = 'a'; t='a'

s = 'a'; t = 'aa'

ans = minWindow(s, t)
print(ans)
