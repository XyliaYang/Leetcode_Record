# @Time : 2020/9/6 10:37
# @Author : Xylia_Yang
# @Description :


class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def  dfs(arr_3,arr_1,hasRelation):
    if len(arr_3)<0 and len(arr_1)<0:
        hasRelation[0]=False

    if len(arr_3)>0:
        root=TreeNode(3)
        arr_3.pop()

        root.left=dfs(arr_3,arr_1,hasRelation)
        root.right=dfs(arr_3,arr_1,hasRelation)

    elif len(arr_1)>0:
        root=TreeNode(1)
        arr_1.pop()
    return  root



if __name__ == '__main__':
    n=int(input())

    a_input=input()
    a_arr=[int(n) for n in a_input.split(' ')]

    hasRelation=[True]
    num_3=0
    num_1=0

    for i in a_arr:
        if i!=3 and i!=1:
            hasRelation[0]=False
        if i==3:
            num_3+=1
    num_1=len(a_arr)-num_3

    arr_3=[3 for i in range(num_3)]
    arr_1=[1 for i in range(num_1)]

    dfs(arr_3,arr_1,hasRelation)

    if hasRelation[0]:
        print("YES")
    else:
        print("NO")
