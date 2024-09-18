# https://leetcode.com/problems/longest-palindrome/

from collections import Counter
from functools import partial
from operator import and_


def longestPalindrome(s: str) -> int:
    """Conventional"""
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
    return


class Solution2:
    def longestPalindrome(self, s: str) -> int:
        """Functional Programming"""

        def even_or_floor(n):
            """return n if n is even else return nearest floor-even for n"""
            return (n // 2) * 2

        (*charFreqs,) = Counter(s).values()

        # check if any character repeats odd times
        isOdd = partial(and_, 1)
        anyCharWithOddCnt = any(map(isOdd, charFreqs))

        # total even char count possible
        palindromeWithEvenCharsLen = sum(map(even_or_floor, charFreqs))

        if anyCharWithOddCnt:
            return palindromeWithEvenCharsLen + 1

        return palindromeWithEvenCharsLen


class Solution3:
    def longestPalindrome(self, s: str) -> int:
        """Better Logic via HashSet"""
        seen = set()
        res = 0

        for char in s:
            if char in seen:
                # second occurence of char
                res += 2
                seen.remove(char)  # reset for more such occurences
            else:
                seen.add(char)

        return res + 1 if seen else res


s = "abccccdd"
s = "a"
s = "bb"
s = "ccc"
s = "fdfdeeeba"
s = "racecar"
ans = longestPalindrome(s)

print(ans)
