# https://leetcode.com/problems/relative-sort-array/

from typing import List


def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
    # map for arr2 :  val -> idx
    idx_map = dict([(v,i) for i,v in enumerate(arr2)]) 
    s2 = len(arr2)
    
    # respect oredering of arr2 element on priority & for rest do normal sorting
    def get_key(v): 
        return idx_map.get(v, s2+v)
    
    # sort the array with custom key inplace to save space
    arr1.sort(key=get_key)
    
    return arr1

arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]

relativeSortArray(arr1, arr2)