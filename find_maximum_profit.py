def maxProfit(prices):
    max_profit = 0
    min_price = float('inf')

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

prices = [1,2,3,4,5]
print(maxProfit(prices))