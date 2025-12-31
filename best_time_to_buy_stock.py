prices = [5, 1, 5, 6, 7, 1, 10]
max_profit = 0
if len(prices) == 0:
    print(0)
else:
    l, r = 0, 1

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        else:
            l = r
        r += 1
    print(max_profit)
