# https://leetcode.com/problems/valid-palindrome/

# def isAlphaNum():
#     #regex = r"^[a-zA-Z\d]$"
#     regex = r"[a-zA-Z\d]"
#     return bool(re.fullmatch(regex, c))

def isPalindrome(s: str) -> bool:
    l, r = 0, len(s)-1
    while l < r:
        print(l, r)
        lc, rc = s[l], s[r]
        if not lc.isalnum(): 
            l = l+1
            continue 
        if not rc.isalnum():
            r = r-1
            continue
        if lc.lower() != rc.lower():
            return False 
        l, r = l+1, r-1
    return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))