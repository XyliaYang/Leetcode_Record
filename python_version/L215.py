# @Time : 2020/3/30 15:52
# @Author : Xylia_Yang
# @Description :

class Solution:
    def findKthLargest(self, nums, k) :
        if not nums or len(nums)-k<0:
            return None

        return  self.quickSort(nums,0,len(nums)-1,len(nums)-k)

    def quickSort(self,nums,left,right,target_index):
        if left<right:
            pivot=self.partition(nums,left,right)

            if pivot==target_index:
                return nums[pivot]
            elif pivot<target_index:
                return self.quickSort(nums,pivot+1,right,target_index)
            else:
                return self.quickSort(nums,left,pivot-1,target_index)
        return nums[target_index]


    def partition(self,nums,left,right):
        """
        找到第一个元素存放的位置，并修改数组
        """
        pivot_key=nums[left]

        while left<right:
            while right>left and nums[right]>=pivot_key:
                right-=1
            nums[left]=nums[right]
            while left<right and nums[left]<=pivot_key:
                left+=1
            nums[right]=nums[left]

        nums[left]=pivot_key
        return left


if __name__=='__main__':
    solution=Solution()
    nums=[3,2,3,1,2,4,5,5,6]
    k=4
    print(solution.findKthLargest(nums,k))