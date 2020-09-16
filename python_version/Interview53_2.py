# @Time : 2020/3/13 19:42
# @Author : Xylia_Yang
# @Description :

class Solution:
    def missingNumber(self, nums):
        if not nums:
            return

        return  self.missNumber(nums,0,len(nums)-1)

    def  missNumber(self,nums,start,end):
        mid=int((start+end)/2)

        if nums[mid]!=mid and (mid==0 or nums[mid-1]==mid-1):
            return mid

        if start<end:
            if mid-1>=0 and nums[mid]!=mid and nums[mid-1]!=mid-1:
                return self.missNumber(nums,start,mid-1)
            if arr[mid]==mid:
                return self.missNumber(nums,mid+1,end)
        return -1

if __name__=='__main__':
    arr=[0,1,3,4,5,6,7]
    solution=Solution()
    print(solution.missingNumber(arr))


