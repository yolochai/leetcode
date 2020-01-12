#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/12 9:11 下午
# @Author  : yc
# @File    : best_time_to_buy_and_sell_stocks_ii.py
# @Software: PyCharm

# original solution
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if not prices:
#             return 0
#         profit = 0
#         buy = prices[0]
#         for i in range(len(prices)):
#             if prices[i] > buy and (i == len(prices) - 1 or prices[i + 1] < prices[i]):
#                 profit += prices[i] - buy
#                 buy = prices[i]
#             else:
#                 buy = min(buy, prices[i])
#         return profit

# better solution
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cnt = 0
        for i in range(1,len(prices)):
            cnt += max(prices[i]-prices[i-1],0)
        return cnt