#https://leetcode.com/problems/number-of-senior-citizens/

from typing import List
import cardinality


def getAgeA1(pax):
    # 12 & 13th char determines age
    return pax[11:13]

def getAgeA2(pax):
    # 12 & 13th char determines age
    return pax[11] + pax[12] 

def getAge(pax):
    # 12 & 13th char determines age
    t = ord(pax[11]) - ord('0')  # tens-place
    u = ord(pax[12]) - ord('0')  # unit-place
    age = (t * 10) + u 
    return age

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        #cardinality.count(filter(isMoreThan60, details))
        return len([None for e in details if getAge(e) > 60])