# @Time : 2020/2/28 15:03
# @Author : Xylia_Yang
# @Description :

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> list[list[int]]:
        if  not TreeNode:
            return []

        res=[]
        stack=[]
        cur_sum=0

        self.getPathSum(root,stack,cur_sum,sum,res)
        return res

    def getPathSum(self,root,stack,cur_sum,sum,res):
        cur_sum+=root.val
        stack.append(root.val)

        if self.isLeaf(root) and cur_sum==sum:
            path=[]
            for i in stack:
                path.append(i)
            res.append(path)

        if root.left:
            self.getPathSum(root.left,stack,cur_sum,sum,res)
        if root.right:
            self.getPathSum(root.right,stack,cur_sum,sum,res)

        # ！！遍历完之后，要记得删除当前路径上的节点
        cur_sum -= root.val
        stack.pop(-1)


    def isLeaf(self,root):
        if root.left or root.right:
            return False
        else:
            return True


