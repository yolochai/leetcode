#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/11 12:10 上午
# @Author  : yc
# @File    : range_num_of_bst.py
# @Software: PyCharm


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        stack = []
        cur_node = root
        res = 0
        while (cur_node is not None) or stack:
            if cur_node is not None and L<=cur_node.val<=R:
                stack.append(cur_node)
                cur_node = cur_node.left
            elif cur_node is not None and cur_node.val<L:
                cur_node = cur_node.right
            elif cur_node is not None and cur_node.val>R:
                cur_node = cur_node.left
            else:
                cur_node = stack.pop()
                res += cur_node.val
                cur_node = cur_node.right
        return res