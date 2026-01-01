# Buy and Sell Stock 

# Brute Force

def maxProfit(prices):
    """
    Calculates maximum profit using a brute force approach.

    Problem:
    Best Time to Buy and Sell Stock.
    Given an array of prices, find the maximum profit by buying on one day and selling on a future day.

    Approach:
    - Iterate through all possible pairs of buy and sell days.
    - Calculate profit for each pair and update the maximum profit.

    Time Complexity: O(N^2)
    - Loops run N * (N-1) / 2 times.

    Space Complexity: O(1)
    """
    max_profit = 0

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i]
    return max_profit
        


# Optimal Solution
def maxProfit(prices):
    """
    Calculates maximum profit using an optimal one-pass approach.

    Problem:
    Best Time to Buy and Sell Stock.

    Approach:
    - Iterate through the prices once.
    - Keep track of the lowest price found so far (`bestBuy`).
    - Calculate the profit if sold today (`price - bestBuy`).
    - Update `maxProfit` if the current profit is higher.

    Time Complexity: O(N)
    - Single pass through the list.

    Space Complexity: O(1)
    """

    maxProfit=0
    bestBuy=prices[0]

    for i in range(len(prices)):
        if prices[i]>bestBuy:
            maxProfit=max(maxProfit,prices[i]-bestBuy)
        bestBuy=min(bestBuy,prices[i])
    return maxProfit



p=[7,1,5,3,6,4]
print(maxProfit(p))
