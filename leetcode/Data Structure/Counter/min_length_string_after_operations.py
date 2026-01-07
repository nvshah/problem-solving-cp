#https://leetcode.com/problems/minimum-length-of-string-after-operations/description/
from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        # At the end it can residue as either 2 or 1 i.e
        # a a a -> 1 element
        # a a a a -> 2 element
        # Hence odd count -> boils down to 1 character end
        # & Even -> boils down to 2 characters at end
        def residue(count):
            return 2 if count % 2 == 0 else 1
        return sum(map(residue, Counter(s).values()))











