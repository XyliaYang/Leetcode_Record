# @Time : 2020/3/13 22:56
# @Author : Xylia_Yang
# @Description :


class Solution(object):
    def getNumberSameAsIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        return self.getSameNumberandIndex(nums,0,len(nums)-1)

    def getSameNumberandIndex(self,nums,start,end):

        mid=int((start+end)/2)
        if mid==nums[mid]:
            return mid

        if start<end:
            if mid<nums[mid]:
                return self.getSameNumberandIndex(nums,start,mid-1)
            if mid>nums[mid]:
                return self.getSameNumberandIndex(nums,mid+1,end)

        return -1

