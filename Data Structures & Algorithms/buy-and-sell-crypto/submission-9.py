class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        index1, index2 = 0, 1
        profit, newProfit = 0, 0
        bestBuyDay = prices[index1]

        while(True):
            if(index2 == len(prices)):
                break
            if(prices[index2] < prices[index1]):
                index1 += 1
            if(prices[index2] >= prices[index1]):
                newProfit = prices[index2] - bestBuyDay
                if(newProfit > profit):
                    profit = newProfit
                index2 += 1
            if (prices[index1] < bestBuyDay):
                bestBuyDay = prices[index1]
            
        
        if (profit > 0):
            return profit
        else:
            return 0

            
            

       