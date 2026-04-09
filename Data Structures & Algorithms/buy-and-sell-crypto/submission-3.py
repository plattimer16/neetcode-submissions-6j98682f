class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length < 2:
            return 0
        res = 0
        minBuy = prices[0]
        for price in prices:
            minBuy = min(minBuy, price)
            print(minBuy, price)
            if price > minBuy:
                res = max(res, price - minBuy)
                print(res)
        return res
