# https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/


class Solution:
    def maxScore(self, s: str) -> int:
        score = 0
        # running score tracked in each trial
        # initially left half there won't be any member
        left = 0
        # initially right half will have all member
        right = s.count("1")
        # skip last position as each half must hold at least element
        for i in range(len(s) - 1):
            
            
            
            left += s[i] == "0"  # left keep tracks of 0
            right -= s[i] == "1"  # right keep tracks of 1
            score = max(score, left + right)
        return score
