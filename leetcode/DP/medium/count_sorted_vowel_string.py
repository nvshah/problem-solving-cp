# https://leetcode.com/problems/count-sorted-vowel-strings/

def countVowelStrings(n: int) -> int:
    ''' DP Approach (via Tabular)'''
    # consider ['a', 'e', 'i', 'o', 'u'] in reverse order for column of dp-table
    # ie ['u', 'o', 'i', 'e', 'a']  // as letter from end is most independent
    # & rows as n-cnt
    
    l = 5
    
    cnts = [1]*l  # representing cnts possible for str of length {l} with starting letter as mentioned above at any moment
    
    for _ in range(2, n+1):
        for j in range(1, l):
            cnts[j] += cnts[j-1]  # dp pattern observed to fill cells
            
    return sum(cnts)