# https://leetcode.com/problems/decode-ways/

def numDecodings(s: str) -> int:
    ''' Top-Down Approach'''
    dp = {len(s):1}

    def explore(i):
        if i in dp:
            return dp[i]
        if s[i] == "0": # invalid string
            # if string starts with 0 then ways are 0 ie "0121" -> 0 as 0 has no mapping so string is invalid
            return 0 
        
        # explore with 1 digit only
        ways = explore(i+1)
        if (i+1 < len(s)) and (10 <= int(s[i:i+2]) <= 26):
            ways += explore(i+2)
        
        dp[i] = ways 
        return ways
    return explore(0)

# Better Approach
def numDecodings2(s: str) -> int:
    ''' Bottom-Up Approach'''
    if s[0] == "0":  # Edge Case 
        return 0
        
    dp = {len(s):1}

    for i in range(len(s)-1, -1, -1):
        if s[i] == "0": # invalid string
            # if string starts with 0 then ways are 0 ie "0121" -> 0 as 0 has no mapping so string is invalid
            dp[i] = 0
        else:
            dp[i] = dp[i+1] # simply considering 1 digit

        # explore for 2 digits
        if (i+1 < len(s)) and (10 <= int(s[i:i+2]) <= 26):
            dp[i] += dp[i+2]
    return dp[0]

s = "12"
s = "226"
s = "0"
s = "06"
ans = numDecodings2(s)
print(ans)