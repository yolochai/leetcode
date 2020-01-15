#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/15 9:49 下午
# @Author  : yc
# @File    : house_robber_ii.py
# @Software: PyCharm

# 执行用时 :24 ms, 在所有 Python 提交中击败了42.45%的用户
# 内存消耗 :11.7 MB, 在所有 Python 提交中击败了27.52%的用户
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        def _rob(subnums):
            max_money,max_money_1,max_money_2 = 0,0,0
            for i in range(len(subnums)):
                max_money = max(max_money_2+subnums[i],max_money_1)
                max_money_2 = max_money_1
                max_money_1 = max_money
            return max_money_1
        return max(_rob(nums[1:]),_rob(nums[:-1]))