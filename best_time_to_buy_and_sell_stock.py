# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

from typing import List


def maxProfit(prices: List[int]) -> int:
    """
    Think about this sol as 2 pointers.
    right = iterating thru the array
    left = keep track of min_price

    Time O(n), Space O(1)
    """
    min_price = float("inf")
    max_profit = 0
    for p in prices:
        if p < min_price:
            min_price = p
        max_profit = max(max_profit, p - min_price)

    return max_profit


print(maxProfit([7, 1, 5, 3, 6, 4]) == 5)
print(maxProfit([7, 6, 4, 3, 1]) == 0)
print(maxProfit([7, 7, 7, 7]) == 0)
print(maxProfit([7, 8, 5, 12, 1, 6, 4]) == 7)
print(maxProfit([7, 2, 5, 3, 6, 4, 1, 2, 1, 5, 10, 4, 8]) == 9)
print(maxProfit([10, 7, 0, 1, 4, 1, 0, 7, 10]) == 10)
print(maxProfit([7]) == 0)
