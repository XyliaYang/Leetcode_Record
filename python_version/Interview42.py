# @Time : 2020/3/9 17:27
# @Author : Xylia_Yang
# @Description :


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums:
            return

        sum=max=nums[0]
        if len(nums)>1:
            for i in nums[1:]:
                if sum < 0:
                    sum = i
                else:
                    sum += i
                if sum > max:
                    max = sum

        return max
