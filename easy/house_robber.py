#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/15 9:38 下午
# @Author  : yc
# @File    : house-robber.py
# @Software: PyCharm

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_money_2 = 0 # 前两家
        max_money_1 = 0 # 前一家
        for i in range(len(nums)):
            max_money = max(max_money_2+nums[i],max_money_1)
            max_money_2 = max_money_1
            max_money_1 = max_money
        return max_money_1