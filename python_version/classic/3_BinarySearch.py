# @Time : 2020/3/6 17:23
# @Author : Xylia_Yang
# @Description : 二分查找

def BinarySearch(ls,value):
    if not ls :
        return
    return do_BinarySearch(ls,value,0,len(ls)-1)

def do_BinarySearch(ls,value,start_index,end_index):
    mid= int((end_index+start_index)/2)

    if value==ls[mid]:
        return mid
    if value<ls[mid]:
        return do_BinarySearch(ls,value,start_index,mid-1)
    if value>ls[mid]:
        return do_BinarySearch(ls,value,mid+1,end_index)



if __name__=='__main__':
    ls=[2,3,6,4,7]
    value=6
    print(BinarySearch(ls,value))