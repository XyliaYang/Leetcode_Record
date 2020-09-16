# @Time : 2020/3/29 8:45
# @Author : Xylia_Yang
# @Description :

class Solution:
    def findTargetSumWays(self, nums: list[int], S: int) -> int:
        self.count=0

        def dfs(nums,length,pos,sum,S):
            if not pos:
                sum+=-nums[length]
            else:
                sum+=nums[length]

            if length==len(nums)-1:
                if sum==S:
                    self.count+=1
                return

            if length+1<len(nums):
                dfs(nums,length+1,True,sum,S)
                dfs(nums,length+1,False,sum,S)


        dfs(nums,0,True,0,S)
        dfs(nums,0,False,0,S)
        return self.count

