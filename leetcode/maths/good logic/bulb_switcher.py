# https://leetcode.com/problems/bulb-switcher/description/
from math import isqrt

'''
QUE

There are n bulbs that are initially off. You first turn on all the bulbs, 
then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). 
For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds.

'''

'''
Explanation

n rounds :
At the end of n rounds the bulb will keep glowing if its toggled odd number of times

In every run ie {r}, the bulb that is divisble by {r} will be toggled

So toggle count for each bulb {b} := #divisors of that bulb-number {b}

Now, (REMEMBER)
> factors of each integer number is always EVEN unless that number is [Perfect Square], 
  in which case it would be ODD (as x*x = x**2)

So all the perfect squares in [1, n] will have odd factors & thus 
corresponding bulb-numbers will glow at the end of round {n}

'''

class Solution:
    def bulbSwitch(self, n: int) -> int:
        return isqrt(n)