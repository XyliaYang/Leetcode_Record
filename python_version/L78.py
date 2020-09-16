# @Time : 2020/3/29 14:09
# @Author : Xylia_Yang
# @Description :

class Solution:
    def subsets(self, nums):
        if not nums:
            return [[]]

        self.res=[[]]


        def subCore(cur,nums,sub_index):
            if sub_index<len(nums):
                for i_index in range(sub_index, len(nums)):
                    self.res.append(cur + [nums[i_index]])

                    if i_index+1<len(nums):
                        subCore(cur + [nums[i_index]], nums,i_index+1 )

            return
        subCore([],nums,0)
        return self.res

if __name__=='__main__':
    solution=Solution()
    nums=[1,2,3]
    print(solution.subsets(nums))