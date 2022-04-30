# https://leetcode.com/problems/online-stock-span/

class StockSpanner1:
    ''' MEMOIZATIO DP WAY '''

    def __init__(self):
        self.prices = [float("inf")]
        self.spans = []

    def next(self, price: int) -> int:
        i = -1  # pointer that move in backward direction to find ideal day of span
        while self.prices[i] <= price:  # till ideal cosnecutive day is found in backwards direction
            lastSpan = self.spans[i]    # grab last/prev day span
            i -= lastSpan               # update current pointer
        self.prices.append(price)       # track the price for current day
        self.spans.append(-i)           # track the span (:= pointer move by) for current price
        return -i                       # return span for cur-price


class StockSpanner2:
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



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


## ------------------------ MY Own Functional Impl --------------------------
def onlineStockSpan1(prices):
    ''' Memoization Way '''
    prices.insert(0, float("inf"))
    spans = []
    for i, price in enumerate(prices[1:], 1):
        j = i-1   
        #span = 1
        while prices[j] <= price:  # prices is 1 based indexing
            print(i, j)
            lastSpan = spans[j-1]  # span is 0 based indexing
            j -= lastSpan
            #span += lastSpan
        span = i-j
        spans.append(span)
    return spans




if __name__ == '__main__':
    price = [100,80,60,70,60,75,85]
    ans = onlineStockSpan(price)
    print(ans)