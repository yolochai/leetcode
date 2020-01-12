#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/12 10:14 下午
# @Author  : yc
# @File    : best_time_to_buy_and_sell_stock_with_cooldown.py
# @Software: PyCharm

# solution:DP
# sell: current profit after selling
# old_sell: profit after lastlast selling(i-2 day)
# buy: profit after buying(cooldown=1 day, so buy = max(buy,old_sell-prices[i]))
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 0:
            return 0
        buy = -prices[0]  # 当前买入之后的profit
        sell = 0  # 当前卖出之后的profit
        old_sell = 0  # 上次卖出之后的profit

        for i in range(1, len(prices)):
            tmp = sell
            sell = max(sell, buy + prices[i])
            buy = max(buy, old_sell - prices[i])
            old_sell = tmp

        return max(sell, old_sell)