# https://leetcode.com/problems/lemonade-change/description/

from typing import List
from collections import defaultdict


def lemonadeChange(bills: List[int]) -> bool:
    # keep track of fives & tens count for change
    funds = defaultdict(int)

    def update_fund(amount, toDeduct=True):
        funds[amount] += -1 if toDeduct else 1

    def get_change(amount):
        if amount == 5:
            if funds[5]:
                return (5,)
        if amount == 10:
            if funds[10]:
                return (10,)
            if funds[5] >= 2:
                return (5, 5)
        if amount == 15:
            if funds[10] and funds[5]:
                return (5, 10)
            if funds[5] >= 3:
                return (5, 5, 5)
        return None

    for bill in bills:
        # skipping 20 as 20 is not used as denomination for change (so no use of keeping it in funds)
        if bill != 20:
            # # take bill amt
            update_fund(bill, toDeduct=False)

        to_change = bill - 5

        if to_change:
            amts = get_change(to_change)
            if not amts:
                return False
            # deduct change amount
            for amt in amts:
                update_fund(amt)

    return True
