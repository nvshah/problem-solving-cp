# https://leetcode.com/problems/valid-palindrome-ii/

'''
Given a string s, 
return true if the s can be palindrome after deleting at most one character from it.
'''


def isPalindrome1(s: str, l, r) -> bool:
    '''
    s :- string
    l :- start idx (inclusive)
    r :- end idx (inclusive)
    '''
    while l < r:
        if s[l] != s[r]:
            return False 
        l, r = l+1, r-1
    return True 

def isPalindrome2(s):
    return s == s[::-1]

def validPalindrome1(s: str) -> bool:
    ''' allow to remove atmost 1 character '''
    l, r = 0, len(s)-1

    while l < r:
        if s[l] != s[r]:
            # check substring ignoring either characters
            skipL = isPalindrome1(s, l+1, r) # ignore left
            skipR = isPalindrome1(s, l, r-1) # ignore right

            return skipL or skipR
        l, r = l+1, r-1

    return True
