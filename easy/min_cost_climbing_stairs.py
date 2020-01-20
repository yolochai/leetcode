#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/19 10:23 下午
# @Author  : yc
# @File    : min_cost_climbing_stairs.py
# @Software: PyCharm
#
# 执行用时 :40 ms, 在所有 Python 提交中击败了91.74%的用户
# 内存消耗 :11.9 MB, 在所有 Python 提交中击败了37.94%的用户

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        res_1,res_2=0,0

        for item in cost:
            tmp = min(res_1+item,res_2+item)
            res_2 = res_1
            res_1 = tmp
        return min(res_1,res_2)