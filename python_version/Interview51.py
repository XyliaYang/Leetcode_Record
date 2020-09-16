# @Time : 2020/3/12 11:14
# @Author : Xylia_Yang
# @Description :

class Solution(object):
    def inversePairs(self, nums):
        if not nums:
            return 0

        temp=[i for i in nums]
        return self.mergeSort(temp,nums,0,len(nums)-1)

    def mergeSort(self,temp,nums,start,end):
        """
        将nums数组left到right的数字排序之后放入temp
        并将逆序对数给返回
        """
        if start>=end:
            temp[start]=nums[start]
            return 0

        mid=int((start+end)/2)
        left=self.mergeSort(nums,temp,start,mid)
        right=self.mergeSort(nums,temp,mid+1,end)


        i=mid
        j=end
        new_index=end
        inverse_num=0
        while(i>=start and j>=mid+1):
            if nums[i]>nums[j]:
                inverse_num+=j-mid
                temp[new_index]=nums[i]
                i-=1
            else:
                temp[new_index]=nums[j]
                j-=1
            new_index-=1

        while i>=start:
            temp[new_index]=nums[i]
            new_index-=1
            i-=1

        while j>=mid+1:
            temp[new_index]=nums[j]
            new_index-=1
            j-=1

        return left+right+inverse_num



if __name__=='__main__':
    solution=Solution()
    nums=[7,5,6,4]
    print(solution.inversePairs(nums))





        

