# @Time : 2020/3/15 11:07
# @Author : Xylia_Yang
# @Description :

class Solution:
    def singleNumber(self, nums) :

        if not nums:
            return

        temp=0
        for i in nums:
            temp^=i

        left_step=self.find1thByLeftStep(temp)

        num1=num2=0
        for i in nums:
            if self.isBit1ByLeftStep(i,left_step):
                num1^=i
            else:
                num2^=i

        return [num1,num2]

    def find1thByLeftStep(self,num):
        index=0

        while(num&1==0 and index<32):
            num=num>>1
            index+=1
        return index

    def isBit1ByLeftStep(self,num,left_step):
        num=num>>left_step
        return num&1



if __name__=='__main__':
    ls=[1,2,1,3,2,5]
    solution=Solution()

    print(solution.singleNumber(ls))