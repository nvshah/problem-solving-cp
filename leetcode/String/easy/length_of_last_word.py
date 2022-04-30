# https://leetcode.com/problems/length-of-last-word/

def lengthOfLastWord(s: str) -> int:
    s = s.strip()
    l = len(s)
    cnt = 0
    i = l-1
    while i >= 0:
        if s[i] == ' ':
            return cnt
        cnt += 1
        i -= 1
    return cnt