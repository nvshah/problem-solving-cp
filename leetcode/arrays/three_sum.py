# https://leetcode.com/problems/3sum/

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    # 1 sort the array
    nums.sort()
    l = len(nums)
    ans = []
    for i, n in enumerate(nums):
        if i > 0 and n == nums[i-1]:
            # if sakura has tested for val once earlier than skip it
            continue
        
        sakura = nums[i] # first element will be i of Sakura

        # Quest begin for next 2 if possible
        naruto, sasuke = i+1, l-1
        while naruto < sasuke:
            chakra = sakura + nums[naruto] + nums[sasuke]
            if chakra == 0:
                ans.append([sakura, nums[naruto], nums[sasuke]]) # found 1 triplet
                while naruto < sasuke and nums[naruto] == nums[naruto + 1]:
                    # step naruto forward until new number is discovered
                    naruto += 1
                naruto += 1 # now naruto will point to new number
            elif chakra < 0: # naruto step forward
                naruto += 1
            else:            # sasuke step backward
                sasuke -= 1 
    return ans

nums = [-1,0,1,2,-1,-4]
nums = [-2,0,0,2,2]
print(threeSum(nums))