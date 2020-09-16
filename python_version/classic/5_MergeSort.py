# @Time : 2020/3/12 13:48
# @Author : Xylia_Yang
# @Description :归并排序


def MergeSort(L):
    if not L:
        return
    if len(L)==1:
        return L

    mid=int(len(L)/2)
    left=MergeSort(L[0:mid])
    right=MergeSort(L[mid:])

    return  Merge(left,right)

def Merge(left,right):
    sorted=[]

    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sorted.append(left[i])
            i+=1
        else:
            sorted.append(right[j])
            j+=1

    if i<len(left):
        sorted+=left[i:]
    if j<len(right):
        sorted+=right[j:]

    return sorted


if __name__=='__main__':
    ls=[5,3,0,6,1,4]
    print(MergeSort(ls))