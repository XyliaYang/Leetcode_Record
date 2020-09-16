# @Time : 2020/2/19 17:25
# @Author : Xylia_Yang
# @Function :

def reorderOddEven(arr):
    if arr is None:
        return
    start=0
    end=len(arr)-1

    while start<end:
        while start<len(arr) and arr[start]%2==1:
            start+=1
        while end>=0 and arr[end]%2==0:
            end-=1

        if start<end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp


def  reorder(arr,isEven):
    if arr is None:
        return
    start=0
    end=len(arr)-1

    while start<end:
        while isOdd(arr[start]):
            start+=1
        while not isOdd(arr[end]):
            end-=1

        if start<end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp

def  isOdd(num):
    return num&1

if __name__=='__main__':
    arr=[1,2,3,4,5]
    reorder(arr,isOdd)
    print(arr)





