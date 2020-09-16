# @Time : 2020/3/16 15:27
# @Author : Xylia_Yang
# @Description :

# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if not array:
            return []

        start=0
        end=len(array)-1

        while start<len(array) and end >=0 and start<end:
            sum=array[start]+array[end]
            if sum==tsum:
                return [array[start],array[end]]

            elif sum<tsum:
                start+=1
            else:
                end-=1
        return []
