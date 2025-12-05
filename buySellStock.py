# Buy and Sell Stock 

# Brute Force

def maxProfit(prices):
    max_profit = 0

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i]
    return max_profit
        


# Optimal Solution
def maxProfit(prices):

    maxProfit=0
    bestBuy=prices[0]

    for i in range(len(prices)):
        if prices[i]>bestBuy:
            maxProfit=max(maxProfit,prices[i]-bestBuy)
        bestBuy=min(bestBuy,prices[i])
    return maxProfit



p=[7,1,5,3,6,4]
print(maxProfit(p))