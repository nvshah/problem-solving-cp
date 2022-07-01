# https://leetcode.com/problems/search-suggestions-system/

from typing import List

def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
    '''2 Pointers  :- O(nlogn + n + k)'''
    l, r = 0, len(products)-1
    
    res = []
    
    products.sort()
    
    for i, c in enumerate(searchWord):
        while l<=r and ((i >= len(products[l])) or (products[l][i] != c)):
            l += 1
        
        while l<=r and ((i >= len(products[r])) or (products[r][i] != c)):
            r -= 1 
        
        e = min(3, r-l+1)
        res.append(products[l:l+e])
        
    return res