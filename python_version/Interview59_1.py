# @Time : 2020/3/16 23:27
# @Author : Xylia_Yang
# @Description :


# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        if not num or len(num)-size<0 or size==0:
            return []

        return [max(num[i:i+size]) for i in range(len(num)-size+1)]


    