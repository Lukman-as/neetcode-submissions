class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        for i in range(len(prices)):
            maxVal = 0
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    maxVal = max(maxVal, prices[j] - prices[i])
            profits.append(maxVal)

        return max(profits)




        


            



        