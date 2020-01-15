#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/14 11:36 下午
# @Author  : yc
# @File    : maximum_subarray.py
# @Software: PyCharm

"""
执行用时 :
28 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗 :
12.3 MB, 在所有 Python 提交中击败了32.76%的用户
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        old_sum = nums[0]
        for i in range(1,len(nums)):
            old_sum = max(max_sum,old_sum)
            max_sum = max(max_sum+nums[i],nums[i])
        return max(old_sum,max_sum)