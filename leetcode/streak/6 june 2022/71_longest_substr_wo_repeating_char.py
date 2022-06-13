# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(s: str) -> int:
    chrs = set()
    l = 0  # window left pointer
    size = 0
    for r in range(len(s)):  # r -> window right pointer
        rc = s[r]
        if rc in chrs:
            while True:    # remove all character till window contain unnique chrs
                lc = s[l]
                chrs.remove(lc)
                l += 1
                if lc == rc:  # check if duplicate chr
                    break
        chrs.add(rc)
        size = max(size, r-l+1)  # update optimal window size
    return size