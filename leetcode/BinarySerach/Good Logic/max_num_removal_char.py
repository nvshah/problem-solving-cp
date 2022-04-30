# https://leetcode.com/problems/maximum-number-of-removable-characters/

from typing import List


def maximumRemovals(s: str, p: str, removable: List[int]) -> int:

    def isSubStr(string, substr, ignore):
        # 2 pointer pointing to 2 strings
        p1, p2 = 0, 0
        s1Len, s2Len = len(string), len(substr)

        while p1 < s1Len and p2 < s2Len:
            if (p1 in ignore) or (string[p1] != substr[p2]):
                # character at p1 & p2 are not same or p1 is discarded char at moment 
                p1 += 1 
            else:
                # character at p1 & p2 are same 
                p1, p2 = p1+1, p2+1
        
        return p2 == s2Len  # ie substr is entirely traveresed by {p2} then only its presennt in string

    l, r = 0, len(removable)-1
    ans = 0
    # As we need to find first k indices from removalbels we can use binary search for this
    while l <= r:
        m = (l + r) // 2
        ignorables = set(removable[:m+1])
        if isSubStr(s, p, ignorables):
            # so first m indices removal satisfy that p is substring of s
            #ans = max(ans, m+1)  # ith index = i+1 number in count
            ans = m+1
            # so lets check if more possible (via adding more indices in ignorable list)
            l = m+1
        else:
            # need to reduce removable indices as first m indices removal not satisfies the p as substring of s
            # so let try to reduce current ignorable indices 
            r = m-1
        
    return ans
        

        
