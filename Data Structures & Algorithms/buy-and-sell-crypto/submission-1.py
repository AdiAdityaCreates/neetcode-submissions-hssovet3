class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
       l = 0
       r = 1
       res = 0
       for i in range(1,len(prices)):
        if prices[l] < prices[r]:
            res = max(res,prices[r]-prices[l])
        else:
            l = r
        r += 1
       return res 