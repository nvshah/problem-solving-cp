# https://leetcode.com/problems/water-bottles/


def numWaterBottles(numBottles: int, numExchange: int) -> int:
    """
    T.C := log (numBottles) with base (numExchange)
    """
    consumed = numBottles
    empty = numBottles
    while empty >= numExchange:
        exchanged, remains = divmod(empty, numExchange)
        consumed += exchanged
        empty = exchanged + remains
    return consumed


def numWaterBottles(numBottles: int, numExchange: int) -> int:
    """
    Every time in case of exchange we are removing numExchange in place of 1 i.e effecevily we are removing only numExchange-1 bottles keeping 1 bottle aside
    T.C := O(1)
    """
    # numBottles - 1 := as we kept replaced bottle aside from begin
    # numExchange - 1  := as effectively this much bottles getting eliminated in each exchange
    exchanged = (numBottles - 1) // (numExchange - 1)
    return numBottles + exchanged


ans = numWaterBottles(9, 3)
