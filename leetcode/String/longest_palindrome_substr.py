# https://leetcode.com/problems/longest-palindromic-substring/

def longestPalindrome(s: str) -> str:
    # [starti, endi, len_substr] 
    helper = [0, 0, 0]  # s, e, len
    size = len(s)

    def updateHelper(l, r):
        '''
        expands from center to check maximum palindrome possible
        '''
        while (l >= 0 and r < size) and (s[l] == s[r]):
            l, r = l-1, r+1

        l, r = l+1, r-1  # correct bound for discovered substring
        length = r-l+1
        if length > helper[2]:
            helper[0], helper[1] = l, r 
            helper[2] = length

    for i in range(size):
        # odd length check (with i as center)
        updateHelper(i-1, i+1)

        # even length palindrome substr check 
        updateHelper(i, i+1)

    return s[helper[0]:helper[1]+1]

def longestPalindrome2(s: str) -> str:
    bound = 0, 0
    resLen = 0
    size = len(s)

    def updatePalindromeBounds(l, r):
        '''
        expands from center to check maximum palindrome possible
        '''
        nonlocal bound, resLen
        while (l >= 0 and r < size) and (s[l] == s[r]):
            l, r = l-1, r+1
        
        l, r = l+1, r-1  # correct bound for discovered substring
        length = r-l+1
        if length > resLen:
            bound = l, r 
            resLen = length

    for i in range(size):
        # odd length check (with i as center)
        l, r = i-1, i+1 
        updatePalindromeBounds(l, r)

        # even length palindrome substr check 
        l, r = i, i+1
        updatePalindromeBounds(l, r)
    
    return s[slice(bound[0], bound[1]+1)]

s = "babad"
s = "cbbd"
print(longestPalindrome(s))