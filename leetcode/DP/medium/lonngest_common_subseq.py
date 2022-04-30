# https://leetcode.com/problems/longest-common-subsequence/

def longestCommonSubsequence(text1: str, text2: str) -> int:
    '''
    LCS - Bottom Up DP :- (Reverse Order) ie Right to Left
    '''

    l1, l2 = len(text1), len(text2)

    # dp[i][j] -> denote the LCS from starting i (text1) & j (text2) to end
    #             from i -> end & j -> end what is max LCS possible

    # (+1) to acomodate the entire strings ie Dummy Row
    dp = [[0]*(l2+1) for _ in range(l1+1)] 


    for i in range(l1-1, -1, -1):      # moving from Right -> Left
        for j in range(l2-1, -1, -1): 
            if text1[i] == text2[j]:  # same
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])

    return dp[0][0]

def longestCommonSubsequence2(text1: str, text2: str) -> int:
    '''
    LCS - DP :- (In-Order) ie Left to Right
    '''

    l1, l2 = len(text1), len(text2)

    # dp[i][j] -> denote the LCS uptil starting i (text1) & j (text2)
    #             upto start -> i & start -> j what is max LCS possible

    # (+1) to acomodate the entire strings ie Dummy Row
    dp = [[0]*(l2+1) for _ in range(l1+1)] 


    for i in range(1, l1+1):      # moving from Right -> Left
        for j in range(1, l2+1): 
            if text1[i-1] == text2[j-1]:  # same
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[l1][l2]


text1 = "abc"
text2 = "abc"
print(longestCommonSubsequence2(text1, text2))