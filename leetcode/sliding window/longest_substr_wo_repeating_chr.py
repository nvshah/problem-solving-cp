# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(s: str) -> int:
    chrs = set()
    l = 0
    res = 0
    for r in range(len(s)):
        rc = s[r]
        if rc in chrs:
            while True:
                chrs.remove(s[l])
                l += 1
                if s[l-1] == rc:
                    break
        chrs.add(rc)
        res = max(res, r-l+1)
    return res

def lengthOfLongestSubstring2(s: str) -> int:
    chrs = set()
    l = 0   # Sliding Window left ptr -> l
    res = 0
    for r in range(len(s)):  # Sliding Window right ptr -> r
        rc = s[r]     
        while rc in chrs:   # remove duplicate character from window
            chrs.remove(s[l])
            l += 1
        chrs.add(rc)
        res = max(res, r-l+1)  # update window size (optimal)
    return res

s = "abcabcbb"
s = "bbbbb"
print(lengthOfLongestSubstring(s))