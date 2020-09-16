# @Time : 2020/4/3 16:34
# @Author : Xylia_Yang
# @Description :

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0

        dp=[0]*len(nums)

        for i in range(len(nums)):
            small_num=[]
            for j in range(i):
                if nums[j]<nums[i]:
                    small_num.append(dp[j])

            if small_num:
                dp[i]=max(small_num)+1
            else:
                dp[i]=1

        return max(dp)
