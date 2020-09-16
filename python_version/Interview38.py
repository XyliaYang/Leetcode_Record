# @Time : 2020/3/5 21:58
# @Author : Xylia_Yang
# @Description :字符串的排列

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if not nums:
            return
        res=[]
        self.PermuteNums(nums,0,res)

        return  res

    def PermuteNums(self,nums,index,res):
        if index==len(nums)-1:
            one_permute=[]
            for i in nums:
                one_permute.append(i)
            res.append(one_permute)

        for iter_index in range(index,len(nums)):
            item=nums[index]             # 待交换处位置的元素要和自己交换一次，以便保留最初的排序
            nums[index]=nums[iter_index]
            nums[iter_index]=item

            self.PermuteNums(nums,index+1,res)

            item = nums[index]              #要注意交换完了之后还要替换回来，以便原来位置处的数字能和其他位置处数字也交换
            nums[index] = nums[iter_index]
            nums[iter_index] = item






