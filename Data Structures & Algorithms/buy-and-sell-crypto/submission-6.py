class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0

        minprice=float('inf')
        maxprice=0

        for i in range(0,len(prices)):
            currentprice=prices[i]
        
            if currentprice < minprice:
                minprice=currentprice

            elif currentprice - minprice > maxprice:
                maxprice=currentprice - minprice

        return maxprice
