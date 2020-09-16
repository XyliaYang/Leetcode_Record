# @Time : 2020/3/1 17:25
# @Author : Xylia_Yang
# @Description :快排

def quick_sort(L):
    if not  L:
        return
    return do_quick(L,0,len(L)-1)

def do_quick(L,start_index,end_index):
    if start_index<end_index:
        pivot = Partition(L, start_index, end_index)
        do_quick(L,start_index,pivot-1)
        do_quick(L,pivot+1,end_index)
    return L

def Partition(L,start_index,end_index):
    pivot_key=L[start_index]

    while start_index<end_index:
        while start_index<end_index and L[end_index]>=pivot_key:

            end_index-=1
        L[start_index]=L[end_index]
        while start_index<end_index and L[start_index]<=pivot_key:
            start_index+=1
        L[end_index]=L[start_index]
    L[start_index]=pivot_key
    return start_index

if __name__=='__main__':
    L = [3,2,3,1,2,4,5,5,6]
    print(quick_sort(L))



