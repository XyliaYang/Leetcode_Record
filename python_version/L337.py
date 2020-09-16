# @Time : 2020/3/25 10:21
# @Author : Xylia_Yang
# @Description :

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        res=self.robCore(root)

        return max(res)

    def robCore(self,root):
        if not root:
            return [0,0]

        left=self.robCore(root.left)
        right=self.robCore(root.right)

        res=[0,0]
        res[0]=max(left[0],left[1])+max(right[0],right[1])
        res[1]=left[0]+right[0]+root.val

        return res