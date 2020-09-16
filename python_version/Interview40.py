# @Time : 2020/3/8 10:29
# @Author : Xylia_Yang
# @Description :最小的k个数


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):

        if not tinput or k<1 or len(tinput)<k:
            return

        start_index=0
        end_index=len(tinput)-1
        res=[]

        pivot=self.Partition(tinput,start_index,end_index)
        while pivot!=k-1:
            if pivot>k-1:
                end_index=pivot-1
                pivot=self.Partition(tinput,start_index,end_index)
            else:
                start_index=pivot+1
                pivot=self.Partition(tinput,start_index,end_index)

        for  i in range(k):
            res.append(tinput[i])
        return  res


    def  Partition(self,ls,start_index,end_index):
        pivot_key=ls[start_index]

        while start_index<end_index:
            while start_index<end_index and ls[end_index]>pivot_key:
                end_index-=1
            ls[start_index]=ls[end_index]
            while start_index<end_index and  ls[start_index]<pivot_key:
                start_index+=1
            ls[end_index]=ls[start_index]

        ls[start_index]=pivot_key
        return start_index



if  __name__=='__main__':
    arr=[19,4,10,9,8,7,5]
    k=5
    solution=Solution()
    print(solution.GetLeastNumbers_Solution(arr,k))