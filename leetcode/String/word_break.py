# https://leetcode.com/problems/word-break/

from typing import List
import re


def wordBreak_d(s: str, wordDict: List[str]) -> bool:
    ''' Wrong Approach '''
    wordDict.sort(key=len, reverse=True)
    piped_wl = '|'.join(wordDict)
    subst = ""  
    regex = r"({})+".format(piped_wl)
    result = re.sub(regex, subst, s, 0)
    #res = re.fullmatch(regex, s)
    print(result)
    return not bool(result)

def wordBreak(s: str, wordDict: List[str]) -> bool:
    ''' Using Bottom Up DP '''
    
    # follow up assumptions to be true i.e empty string is available
    size = len(s)
    dp = [False]*(size+1)
    dp[size] = True 

    for i in range(size-1, -1, -1):
        # check all possible words:
        for w in wordDict:
            w_size = len(w)
            if s[i:i+w_size] == w:
                # print(i, w_size)
                # print(dp)
                dp[i] = dp[i + w_size]  # check if string after this word is breakable or not
                if dp[i]:
                    break  # as for current idx found sufficient breakable predicate

    return dp[0]
    


s = "leetcode"
wordDict = ["leet", 'code']

# s = "applepenapple"
# wordDict = ["apple","pen"]

# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]

# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
# wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

a = wordBreak(s, wordDict)
print(a)