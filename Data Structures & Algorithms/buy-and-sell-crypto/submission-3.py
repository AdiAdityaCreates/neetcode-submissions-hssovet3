class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
       
       diff = 0
       res = 0
       cur  = 0
       l = 0
       for r  in range(1,len(prices)):
        diff  = prices[r] - prices[r-1]
        cur = max(0,cur + diff)

        res = max(res,cur)
       return res
        