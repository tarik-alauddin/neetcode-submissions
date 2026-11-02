class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        res = 0
        L = 0
        R = 1

        while R < len(prices):
            profit = prices[R] - prices[L]
            res = max(res, profit)

            if profit <= 0:
                L += 1
                R = L + 1
            elif profit > 0:
                R += 1

        return res
            