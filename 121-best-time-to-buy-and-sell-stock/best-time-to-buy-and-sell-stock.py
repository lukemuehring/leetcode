class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (len(prices) < 2):
            return 0 

        # # loop through the array and keep track of the current min (buy) and max (sell), store their index
        # minP, maxP = 0, 0
        # profit = 0
        # for i in range(1, len(prices)):
        #     if prices[i] < prices[minP]:
        #         # if (prices[maxP] - prices[minP] > profit):
        #         #     profit = prices[maxP] - prices[minP]
        #         minP = i
        #         maxP = i
            
        #     if prices[i] > prices[maxP]:
        #         maxP = i
        #         if (prices[maxP] - prices[minP]) > profit:
        #             profit = prices[maxP] - prices[minP]

        # return profit

        # Neetcode

        l, r = 0, 1
        profit = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l=r
                r+=1
                continue
            currProfit = prices[r] - prices[l]
            if currProfit > profit:
                profit = currProfit
            r+=1

        return profit
            
            
    

