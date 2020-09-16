# @Time : 2020/2/27 15:31
# @Author : Xylia_Yang
# @Description :

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    ## 32.1 不分行从上到下打印二叉树
    ## Acwing上为返不为null值的list
    def PrintFromTopToBottom(self, root):
        if  not root:
            return  []

        res=[]
        q=[root]
        while  q:
            item=q.pop(0)
            res.append(item.val)

            if  item.left:
                q.append(item.left)
            if  item.right:
                q.append(item.right)
        return res

    ## 32.2 分行从上到下打印二叉树
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
        res=[[]]
        q=[root]
        curNodes=1
        nextNodes=0
        res_index=0 #第几层

        while q:
            if curNodes:
                item=q.pop(0)
                res[res_index].append(item.val)
                curNodes-=1

                if item.left:
                    q.append(item.left)
                    nextNodes+=1
                if item.right:
                    q.append(item.right)
                    nextNodes+=1

            if curNodes==0 and nextNodes:
                curNodes=nextNodes
                nextNodes=0
                res_index+=1
                res.append([])
        return res

    ## 32.3 之字形打印二叉树
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []

        res=[]
        stack_even=[root]
        stack_odd=[]
        level_index =0


        while stack_even or stack_odd:
            res.append([])
            if level_index&1: #奇
                while stack_odd:
                    item=stack_odd.pop()
                    res[level_index].append(item.val)

                    if item.right:
                        stack_even.append(item.right)
                    if item.left:
                        stack_even.append(item.left)

            else: #偶
                while stack_even:
                    item = stack_even.pop()
                    res[level_index].append(item.val)

                    if item.left:
                        stack_odd.append(item.left)
                    if item.right:
                        stack_odd.append(item.right)
            level_index += 1

        return res


if __name__=='__main__':
    solution=Solution()
    tree=TreeNode(2)
    print(solution.PrintFromTopToBottom(tree))
