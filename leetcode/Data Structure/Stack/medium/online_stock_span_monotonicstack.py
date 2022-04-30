# https://leetcode.com/problems/online-stock-span/


class StockSpanner:
    ''' More Advancne Logic 
        STACK BaSED (Monotonic Decreasing STack)
    '''

    def __init__(self):
        self.stack = [] # (price, span) <- element

    def next(self, price: int) -> int:
        span = 1  # default span for any price would be 1
        while self.stack and self.stack[-1][0] <= price:
            e = self.stack.pop()   # remove prev price as its gonna hidden under curr-price stock-span
            span += e[1]
        self.stack.append((price,span))
        return span
