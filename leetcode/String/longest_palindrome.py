# https://leetcode.com/problems/longest-palindrome/

from collections import Counter

def longestPalindrome(s: str) -> int:
    ctr, ans, oddDone = Counter(s), 0, False
    # ans = 0
    # oddDone = False
    for cnt in ctr.values():
        if cnt % 2 == 0:
            # Even
            ans += cnt
        else:
            # Odd
            if cnt > 2:
                ans += cnt - 1
            if not oddDone:
                ans, oddDone = ans + 1, True
    return ans

s = "abccccdd"
s = "a"
s = "bb"
s = "ccc"
s = "fdfdeeeba"
s = "racecar"
ans = longestPalindrome(s)

print(ans)
