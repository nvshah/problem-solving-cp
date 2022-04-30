from collections import Counter as ctr
from typing import List 

def topKFrequent1(nums: List[int], k: int) -> List[int]:
    m = ctr(nums)
    return [i for i,_ in m.most_common(k)]


def topKFrequent2(nums: List[int], k: int) -> List[int]:
    size = len(nums)
    bucket = [[] for i in range(size + 1)]
    freq = ctr(nums)  # freq of each n in nums
    ans = []
    
    # bucket :- freq_cnt -> [ nums having @freq_cnt ]
    for n, cnt in freq.items(): # filling bucket 
        bucket[cnt].append(n)

    for cnt in range(size, -1, -1):
        l = bucket[cnt]  # get all the nums having frequency = cnt
        for n in l:
            ans.append(n)
            if len(ans) == k: # fulfilled & found k freq element
                return ans

nums = [1,1,1,2,2,3]
k = 2

print(topKFrequent2(nums, k))
            


