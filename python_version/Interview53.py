# @Time : 2020/3/13 9:47
# @Author : Xylia_Yang
# @Description :

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1,-1]

        start=self.findFirstTarget(nums,0,len(nums)-1,target)
        end=self.findLastTarget(nums,0,len(nums)-1,target)

        return [start,end]

    def findFirstTarget(self,nums,start,end,target):

        mid=int((start+end)/2)

        if  nums[mid]==target and (mid==0 or nums[mid-1]!=target):
            return mid

        if start<end:
            if  nums[mid]>target or nums[mid]==target and nums[mid-1]==target:
                return self.findFirstTarget(nums,start,mid-1,target)
            if nums[mid]<target:
                return  self.findFirstTarget(nums,mid+1,end,target)

        return -1

    def findLastTarget(self,nums,start,end,target):
        mid=int((start+end)/2)

        if nums[mid]==target and (mid==len(nums)-1 or nums[mid+1]!=target):
            return  mid

        if start<end:
            if  nums[mid]>target:
                return  self.findLastTarget(nums,start,mid-1,target)
            if nums[mid]<target or nums[mid]==target and nums[mid+1]==target:
                return  self.findLastTarget(nums,mid+1,end,target)

        return -1

