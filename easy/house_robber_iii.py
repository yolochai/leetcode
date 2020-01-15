#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/15 10:24 下午
# @Author  : yc
# @File    : house_robber_iii.py
# @Software: PyCharm

# 执行用时 :64 ms, 在所有 Python 提交中击败了11.65%的用户
# 内存消耗 :16 MB, 在所有 Python 提交中击败了19.35%的用户

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def decide(node):
            if not node:
                return 0, 0
            left = decide(node.left)
            right = decide(node.right)
            m1 = left[1] + right[1] + node.val  # 偷
            m2 = max(left) + max(right)  # 不偷
            return m1, m2

        return max(decide(root))
