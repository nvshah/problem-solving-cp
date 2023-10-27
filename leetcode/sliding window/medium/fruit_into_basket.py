# https://leetcode.com/problems/fruit-into-baskets/description/
from typing import List
from collections import defaultdict

def totalFruit(fruits: List[int]) -> int:
    res = 0  # max sub-array size, (ie fruits can be picked continuously)
    counter = defaultdict(int)

    left, total = 0, 0
    for right in range(len(fruits)):
        # account fruit into basket
        counter[fruits[right]] += 1  # individual fruit count in basket
        total += 1 # total fruit count in basket

        # Check basket constriants (of atmost 2 diff type)
        while len(counter) > 2:
            # remove a fruit by moving left ptr ahead
            f = fruits[left]
            counter[f] -= 1  # decrease fruit stock in basket
            total -= 1
            left += 1  

            if counter[f] == 0:
                del counter[f] 
        
        # update optimal window size (ie max sub-array size)
        res = max(res, total)
    return res