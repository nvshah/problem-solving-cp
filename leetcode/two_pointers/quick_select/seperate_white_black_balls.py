# https://leetcode.com/problems/separate-black-and-white-balls/description/

'''
Idea -> Quick Select (ie Partition Step)
'''

class Solution:
    def minimumSteps(self, s: str) -> int:
        # goal put all 0 to left side and all 1 to right side
        left = 0
        swaps = 0
        for right in range(len(s)):
            if s[right] == '0':
                swaps += 1
                left += 1  # next possible pos for 0
        return swaps