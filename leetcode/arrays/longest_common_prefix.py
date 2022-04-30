# https://leetcode.com/problems/longest-common-prefix/

from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    res = ""
    for t in zip(*strs):  # get character of all strings one by one
        c = t[0]   # First Character
        if not all([x==c for x in t]):  # check if all character are same or not
            return res
        res += c
    return res

def longestCommonPrefix2(strs):
    res = [""]
    for t in zip(*strs):  # get character of all strings one by one
        c = t[0]   # First Character
        if not all([x==c for x in t]): break  # characters are not same
        res.append(c)
    return ''.join(res)