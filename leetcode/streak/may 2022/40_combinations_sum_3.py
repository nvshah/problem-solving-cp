# https://leetcode.com/problems/combination-sum-iii/

from typing import List

'''Via BackTracking'''
def combinationSum3(k: int, n: int) -> List[List[int]]:
    nums = [i for i in range(1, 10)]
    l = len(nums)
    s = sum(nums)
    if n > s : return []

    ans = [] 
    trip = []

    def k_sum(k, s, total):
        if k != 2:
            for i in range(s, l):
                n = nums[i]
                # explore
                if n > total:
                    continue
                trip.append(n)
                k_sum(k-1, i+1, total-n)
                # backtrack
                trip.pop()
        else:
            st = set(nums[s:])
            for p1 in nums[s:]:
                p2 = total - p1 
                if p2 <= p1: break  # cannot find (p1, p2) that sum upto {total}
                if p2 in st:
                    ans.append([*trip, p1, p2])
                    st.remove(p1)
                    st.remove(p2)

    k_sum(3, 0, n)
    
    return ans 

k = 3
n = 1
a = combinationSum3(k, n)
print(a)