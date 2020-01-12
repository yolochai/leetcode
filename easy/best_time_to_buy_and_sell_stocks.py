#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/12 8:53 下午
# @Author  : yc
# @File    : best_time_to_buy_and_sell_stocks.py
# @Software: PyCharm

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        profit = 0
        buy = max(prices)
        profit = 0
        for item in prices:
            if item<=buy:
                buy = item
            else:
                profit = max(profit,item-buy)
        return profit