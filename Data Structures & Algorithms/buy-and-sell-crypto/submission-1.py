class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 0
        max_profit = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right

            cur_profit = prices[right] - prices[left]

            max_profit = max(max_profit, cur_profit)
            right += 1

        return max_profit