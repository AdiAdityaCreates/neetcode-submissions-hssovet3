class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0
        cuurent = 0
        for i in range(1,len(prices)):
            diff = prices[i] - prices[i-1]
            cuurent = max(0,cuurent+diff)
            res = max(res,cuurent)
        return res