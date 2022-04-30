# https://leetcode.com/problems/edit-distance/

'''
Idea :- Bottom Up DP (via Matrix Cache)

     Extension of Longest Common SubSequence

Logic :- 

In table 
if for any given word idx i & j for word1 & word2 corresp
if word1[i] == word2[j]
   then -> (i+1, j+1)

else:     // need to peform either of 3 operations
    1     // 1 for performing either of below operation
    +
    Take min from  {right, bottom, diagonal}
     \
      - insert :- (i, j+1)  // ie Right Cell
      - delete :- (i+1, j)  // ie Bottom Cell
      - Replace :- (i+1, j+1)  // ie Diag Cell

'''

def minDistance(word1: str, word2: str) -> int:
    # 1. init cache dp table (1 extra col & 1 extra row at end for base cases)
    #    cell val := Min-num of operations need to transfer word1 into word2
    #    NOTE :- when either one is empty cell val := length of other one
    r, c = len(word1), len(word2)
    inf = float('inf')  # initially assuming we cannot convert from w1 -> w2
    cache = [
        *[[*[inf]*(c), r-i] for i in range(r)], # calc val for last col
        [*[c-i for i in range(c)], 0]  # last row
    ]

    print(cache)

    # 2. Bottom Up DP - Fill table
    for i in range(r-1, -1, -1):
        for j in range(c-1, -1, -1):
            if word1[i] == word2[j]:
                cache[i][j] = cache[i+1][j+1]
            else:
                # check all 3 operations possibility
                a = cache[i][j+1]  # insert
                d = cache[i+1][j]  # delete
                r = cache[i+1][j+1] # replace
                
                e = min(a, d, r)  # effective is min among all 3

                cache[i][j] = 1 + e # 1 to perform either of 3 operations
    
    return cache[0][0]  # min opeerations at begining of both strings


word1 = "horse"
word2 = "ros"

ans = minDistance(word1, word2)
print(ans)