#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/12 10:28 下午
# @Author  : yc
# @File    : best_time_to_buy_and_sell_stock_with_transaction_fee.py
# @Software: PyCharm

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0
        sell = 0
        buy = -prices[0]
        for i in range(1,len(prices)):
            tmp_sell =  sell
            sell =  max(sell,buy+prices[i]-fee)
            buy = max(buy,tmp_sell-prices[i])
        return sell