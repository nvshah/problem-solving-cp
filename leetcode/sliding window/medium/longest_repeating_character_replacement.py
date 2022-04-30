# https://leetcode.com/problems/longest-repeating-character-replacement/

from collections import defaultdict

def characterReplacement(s: str, k: int) -> int:
    '''
        O(n)
        Idea :- Try to explore window  
                Expand -> until It has replacable slots (to make all elements same in window)
                Shrink -> when replacable slots exceeds thresolds {k}
    '''
    counts = defaultdict(int)  # Counter
    res = 0  # max-length of window

    l, size = 0, len(s)
    # max-frequency of element in Window (NOTE :- this should increase as move towards right)
    # max-freq -> Monotonic increasing during exploration
    #          -> As if we need to find max-lenght window then max-freq also increase compare to prev
    
    # optimal window := max-length window possible
    maxF = 0 # max-freq of any element in optimal-Window s[l,r]

    for r in range(size):
        rCnt = counts[s[r]] = counts[s[r]] + 1  # freq update
        maxF = max(maxF, rCnt) # update the max-freq for optimal-window

        windowLen = r-l+1 
        toReplace = windowLen - maxF
        if toReplace > k:
            # shrink window
            counts[s[l]] -= 1
            l += 1

        # update the window length (res)
        res = max(res, r-l+1)  # window length = r-l+1

    return res

s = "ABAB"
k = 2

s = "AABABBA"
k = 1

r = characterReplacement(s, k)
print(r)




