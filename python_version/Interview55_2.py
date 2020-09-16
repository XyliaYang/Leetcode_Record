# @Time : 2020/3/14 11:52
# @Author : Xylia_Yang
# @Description :

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        leftHeight=self.maxDepth(root.left)
        rightHeight=self.maxDepth(root.right)

        if abs(leftHeight-rightHeight)>1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self,root):
        if not root:
            return 0

        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1



class Solution_2:
    def isBalanced(self, root: TreeNode) -> bool:
        self.isbalance=True

        def dfs(root):
            if not root:
                return 0

            left=dfs(root.left)
            right=dfs(root.right)

            if abs(left-right)>1:
                self.isbalance=False
            return max(left,right)+1

        dfs(root)
        return self.isbalance











