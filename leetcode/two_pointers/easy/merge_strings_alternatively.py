# # https://leetcode.com/problems/merge-strings-alternately/description/
import itertools as it

def mergeAlternately(word1: str, word2: str) -> str:
    '''Chain | Zip'''
    pairs = it.zip_longest(word1, word2, fillvalue='')      
    characters = it.chain.from_iterable(pairs)
    return ''.join(characters)

def mergeAlternately2(word1: str, word2: str) -> str:
    '''2 Pointers'''
    S1, S2 = len(word1), len(word2)
    b = min(S1, S2) # break point
    chars = []
    for i in range(b):
        chars.append(word1[i])
        chars.append(word2[i])
    
    chars.extend(word1[b:])
    chars.extend(word2[b:])

    return "".join(chars)



word1 = "abc"
word2 = "pqr"

word1 = "ab"
word2 = "pqrs"

ans = mergeAlternately(word1, word2)
print(ans)