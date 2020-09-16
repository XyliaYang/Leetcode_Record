# @Time : 2020/4/5 9:02
# @Author : Xylia_Yang
# @Description :

class Solution:
    def maxProduct(self, nums) :
        if not nums:
            return None
        if len(nums)==1:
            return nums[0]

        imax=1
        imin=1
        max_num=nums[0]

        for num in nums:
            if num<0:
                temp=imax
                imax=imin
                imin=temp
            imax=max(num,imax*num)
            imin=min(num,imin*num)

            max_num=max(max_num,imax)
        return max_num


if __name__=='__main__':
    solution=Solution()
    ls=[-2,0,-1]
    print(solution.maxProduct(ls))