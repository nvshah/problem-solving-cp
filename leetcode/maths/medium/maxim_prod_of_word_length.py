# https://leetcode.com/problems/maximum-product-of-word-lengths/
from typing import List
from itertools import combinations

def maxProduct(words: List[str]) -> int:
#         vocab = set().union(*words)
#         mp = {c: [] for c in vocab}
        
#         for w in words:
#             for c in w:
#                 mp[c].append(w)
        
#         visit = defaultdict(bool)
#         f = []
#         for k in mp :
#             if len(mp[k]) == 1 and not visit[mp[k][0]]:
#                 f.append(k)
#                 visit[mp[k][0]] = True
            
#         if not f: return 0
#         print(f)
#         v = sorted([mp[k][0] for k in f])
        words.sort(reverse=True)
        elig = [len(e1) * len(e2) for e1, e2 in combinations(words, 2) if not(set(e1) & set(e2))]
        elig.append(0)
        return max(elig)