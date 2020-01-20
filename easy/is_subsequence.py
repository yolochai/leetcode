#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 10:25 下午
# @Author  : yc
# @File    : is_subsequence.py
# @Software: PyCharm

# 执行用时 :140 ms, 在所有 Python 提交中击败了42.01%的用户
# 内存消耗 :17.3 MB, 在所有 Python 提交中击败了53.51%的用户

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        curs, curt = 0, 0
        ls, lt = len(s), len(t)
        while curs < ls and curt < lt:
            if s[curs] == t[curt]:
                curs += 1
                curt += 1
            else:
                while curt < lt and s[curs] != t[curt]:
                    curt += 1
        return curs == ls

