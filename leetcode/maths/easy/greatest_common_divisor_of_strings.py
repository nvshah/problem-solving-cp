# # https://leetcode.com/problems/greatest-common-divisor-of-strings/submissions/

# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         regex1 = fr"^({str2})\1*$"
#         m1 = re.match(regex1, str1)
#         if m1:
#             return str2
        
#         regex2 = r"^(.+)\1*$"
#         m2 = re.match(regex2, str2)
#         if m2.group(0) == str2: return ""
        
#         regex2 = r"^({m2.group(1)})\1*$"
#         m1 = re.match(regex2, str1)
#         if not m1: return ""
        
#         return m2.group(1)
        

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        
        def isDivisor(s):
            l = len(s)
            if l1%l or l2%l:
                return False
            
            # factors
            f1, f2 = l1//l, l2//l
            return (str1 == s*f1) and (str2 == s*f2)
        
        small = str2 if l2 <= l1 else str1
        
        # Greedy so consider biggest first
        for k in range(len(small), 0, -1):
            if isDivisor(small[:k]):
                return small[:k]
        return ""
            
            
            