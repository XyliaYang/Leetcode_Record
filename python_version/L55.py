# @Time : 2020/4/4 9:58
# @Author : Xylia_Yang
# @Description :

class Solution:
    def canJump(self, nums):
        if not nums:
            return False

        max=0
        for i in range(len(nums)):
            if max>=i and i+nums[i]>max:
                max=i+nums[i]

                if max>=len(nums)-1:
                    return True

        return max>=len(nums)-1

if __name__=='__main__':
    solution=Solution()
    ls=[3,2,1,0,4]
    print(solution.canJump(ls))