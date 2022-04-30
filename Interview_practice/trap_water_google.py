# https://leetcode.com/problems/trapping-rain-water/

from typing import List

'''
Logic ->

(Idea partially derived from Quick Sort Approach)

We will find trap of water for each wall. How ??
-> for any wall, trap of water = (minimal longest wall among either side - current wall height)

 To find the minimal longest wall among either side  :- 
 1. find the max wall height on left side 
 2. find the max wall height on right side
 3. take min among above 2 findings
Approach : (Story)
2 Person will start quest from opposite direction
ramesh's task to track max element in his way till he met suresh
suresh's task to track max element in his way till he met ramesh

In this way ramesh will find max element of Left side & suresh will find max element on right side
Also the movement of both ramesh & suresh is decided after they talk with each other &
the person with least val founding will move further.

'''


# def trap(height: List[int]) -> int:
#     # def checkTrap(base_h, base_w, left_h, right_h, i):
#     # # def checkTrap(i, basew):
#     #     if i == 0 or i == l-1:
#     #         return 0
#     #     if left_h > base_h < right_h:
#     #         new_base_h = min(left_h, right_h)
#     #         store_area = new_base_h * base_w
#     #     else:
#     #         return 0
#     #     if left_h == right_h:
#     #         new_base_w = 1 + base_w + 1
#     #         r = i
#     #         return store_area + checkTrap()
#     li = len(height)
#     store_a = 0

#     d = {}
#     for i in range(1, li-1):
#         l, r = i-1, i+1
#         base_h, base_w = height[i], 1
#         participants = [i] 
#         while (0 <= l) and (r <= li-1):
#             left_h = height[l]
#             right_h = height[r]
#             if left_h > base_h < right_h:
#                 b_o = 1
#                 if left_h < right_h:
#                     min_wall_h, l = left_h, l-1
#                     participants.append(l)                
#                 elif left_h > right_h:
#                     min_wall_h, r = right_h, r+1
#                     participants.append(r)
#                 else:
#                     l, r, b_o = l-1, r+1, 2
#                     participants.extend([l, r])

#                 store_h = min_wall_h - base_h
#                 store_a += store_h * base_w
                
#                 base_w = b_o + base_w  # update new base width
#                 base_h = min_wall_h         # update new base height
#             else: 
#                 break
#         for i in participants:
#             height[i] = base_h
#     return store_a

def trap(height: List[int]) -> int:
    '''
        2 Pointers approach  (Divide & Conquer Approach)

        Approach -> need to find largest wall on both of side at present 
                    & then find smallest among them 
                    - then subtract current wall height from foundings

         Ramesh & Suresh on quest of max element | Both possess Walkie-Talkie for communication
         -> ramesh : track the max elem from left part 
            suresh : track the max elem from right part
    '''
    l = len(height)
    ramesh, suresh = 0, l-1
    maxL, maxR = height[ramesh], height[suresh]
    ans = 0

    while ramesh != suresh:  # loop until ramesh & suresh not meet each other
        # who has max at moment 
        if maxL <= maxR:
            # ramesh knows atleast big wall is present on Right Side (by talking with suresh)
            # so ramesh has only to deal with left side max which he's tracking already
            ramesh += 1
            r_h = height[ramesh]
            if maxL > r_h:
                ans += maxL - r_h  # water will be trapped on current wall where ramesh is standing 
            else:
                maxL = r_h         # ramesh's foundings
        else:
            # suresh knows atleast big wall is present on Left Side (by talking with ramesh)
            # so suresh has only to deal with right side max which he's tracking already
            suresh -= 1
            s_h = height[suresh]
            if maxR > s_h:
                ans += maxR - s_h  # water will be trapped on current wall where suresh is standing
            else:
                maxR = s_h         # suresh's foundings
        
    return ans

    

        







height = [0,1,0,2,1,0,1,3,2,1,2,1]
#height = [4,2,0,3,2,5]
ans = trap(height)

print(ans)
                



