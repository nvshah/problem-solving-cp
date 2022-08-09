# https://leetcode.com/problems/count-vowels-permutation/

'''
IDEA :
We will identify the total strings possible via looking the last character
because based on the last character next character is decided
So asa length increases we will decide total next possible strings for next length
'''

def countVowelPermutation2(n: int) -> int:
    # possible string of length 1 that ends with corresp characters 
    a, e, i, o, u = 1, 1, 1, 1, 1
    MOD = 10**9 + 7
    for l in range(n-1):
        # for str of length [l]
        a = (e + i + u) % MOD  # possible str where chars end with [a] 
        e = (a + i) % MOD      # possible str where chars end with [e] 
        i = (e + o) % MOD      # possible str where chars end with [i] 
        o = i % MOD           # possible str where chars end with [o] 
        u = (i + o) % MOD     # possible str where chars end with [u] 
    return (a + e + i + o + u) % MOD 

def countVowelPermutation1(n: int) -> int:
    # dp[j][c] = num of strs of length=j, that ends with char [c]
    dp = [[0]*5,   # with len=0, -> 0
         [1]*5]    # with len=1, -> only 1 possibility for each char

    # Index mapping for each character
    a, e, i, o, u = 0, 1, 3, 4, 5

    MOD = 10**9 + 7

    for j in range(2, n+1):
        cur = [0]*5
        # Update cnt for each character
        prev = dp[j-1]  # prev counts for length=j-1

        cur[a] = (prev[e] + prev[i] + prev[u]) % MOD
        cur[e] = (prev[a] + prev[i]) % MOD 
        cur[i] = (prev[e] + prev[o]) % MOD 
        cur[o] = prev[i] % MOD 
        cur[u] = (prev[i] + prev[o]) % MOD

        dp.append(cur)  # current total strings for each char for lenght=j

    return sum(dp[n]) % MOD