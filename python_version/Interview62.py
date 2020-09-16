# @Time : 2020/3/17 11:26
# @Author : Xylia_Yang
# @Description :



# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):

        if  n<1 or m<1:
            return -1
        nums=[i for i in range(n)]

        index=(m-1)%len(nums)
        while len(nums)>1:
            nums.pop(index)
            index=(index+m-1)%len(nums)

        return nums[0]


if __name__=='__main__':
    solution=Solution()
    n=6
    m=7
    print(solution.LastRemaining_Solution(n,m))




