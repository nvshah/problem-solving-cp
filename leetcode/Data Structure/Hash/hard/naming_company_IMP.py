# https://leetcode.com/problems/naming-a-company/description/
from typing import List
from collections import defaultdict
from itertools import combinations

'''
Idea : 
Generally Brute-Force : Compare every pair of words : O(n^2)
Better: try to reduce pairs for comparision
- Pair having same starting letter, after swapped will create existing words So that can be eliminated
- Between 2 diff letters group, if suffix is common then those words also create existing words when swapped
  Eg t: [onny, ilak], m: [onny, at] 
       => here onny is common so whenever that is paired with other, it will bring existing word into opposite group
 
Steps 
i. group words by same starting letter, creating map of {start-letter: {suffix}}
ii. take pair of groups
iii. for each pair of group 
     -> Eliminate the common suffixes (as those are useless)
     -> Find the count of possible pairs
'''
def distinctNames(ideas: List[str]) -> int:
    distincts = 0

    # Suffix-Map
    groups = defaultdict(set) # start_letter -> set[suffixes]
    for i in ideas:
        groups[i[0]].add(i[1:]) 
    
    for g1, g2 in combinations(groups, 2):
        common = len(groups[g1] & groups[g2])
        unique1 = len(groups[g1]) - common
        unique2 = len(groups[g2]) - common
        pairs = unique1 * unique2 * 2 # 2 for permutation ie (a,b) & (b,a)
        distincts += pairs
    
    return distincts
