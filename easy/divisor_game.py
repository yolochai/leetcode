#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/20 8:24 下午
# @Author  : yc
# @File    : divisor_game.py
# @Software: PyCharm


# 推导
# 数字N如果是奇数，它的约数必然都是奇数；若为偶数，则其约数可奇可偶。
# 无论N初始为多大的值，游戏最终只会进行到N=2时结束，那么谁轮到N=2时谁就会赢。
# 因为爱丽丝先手，N初始若为偶数，爱丽丝则只需一直选1，使鲍勃一直面临N为奇数的情况，这样爱丽丝稳赢；
# N初始若为奇数，那么爱丽丝第一次选完之后N必为偶数，那么鲍勃只需一直选1就会稳赢。
# 综述，判断N是奇数还是偶数，即可得出最终结果！
class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        return not N%2

#动态规划法
class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        res = [0 for i in range(N+1)]
        if N<=1:
            return False
        res[2] =1
        for i in range(3,N+1):
            for j in range(1,i//2):
                if i%j==0 and res[i-j]==0:
                    res[i]=1
                    break
        return res[N]==1
