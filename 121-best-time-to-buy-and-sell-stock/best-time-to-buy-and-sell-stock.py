class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) < 2:
            return profit
    
        # two pointers, left (buy) and right (sell)
        l = 0
        r = 1

        # while r is within the array,
        while r < len(prices):
            # check if r.value < l.value and r > l (index check - you must buy from a day in the future)
            if prices[r] < prices[l]:
                # set l = r, and move r to next index
                l = r
                r += 1
                continue
            # if this purchase is more profitable, save it
            if prices[r] - prices[l] > profit:
                profit = prices[r] - prices[l]
            r += 1
        
        return profit
        
            
            
    

