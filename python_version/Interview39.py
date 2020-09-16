# @Time : 2020/3/8 9:07
# @Author : Xylia_Yang
# @Description :


class Solution:
    def majorityElement(self, nums) :

        if not nums:
            return

        num=nums[0]
        count=1
        for i in nums[1:]:
            if count==0:
                num=i
                count=1

            elif i!=num:
                count-=1
            else:
                count+=1

        if self.isOverHalf(nums,num):
            return num
        else:
            return


    def isOverHalf(self,nums,res):
        count=0
        for i in nums:
            if i==res:
                count+=1

        if count>int(len(nums)/2):
            return  True
        else:
            return  False


if __name__=='__main__':
    solution=Solution()
    arr=[3,2,3]
    print(solution.majorityElement(arr))






