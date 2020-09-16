# @Time : 2020/2/25 17:59
# @Author : Xylia_Yang
# @Description :

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.Symmetric(root,root)
    def Symmetric(self,roo1,root2):
        if not roo1 and not root2:
            return True
        if (roo1 and not root2) or (not roo1 and root2):
            return False
        if roo1.val !=root2.val:
            return False

        return self.Symmetric(roo1.left,root2.right) and self.Symmetric(roo1.right,
                                                                        root2.left)

if __name__=='__main__':
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(2)
    root.left.left=TreeNode(3)
    root.left.right=TreeNode(4)
    root.right.left=TreeNode(4)
    root.right.right=TreeNode(3)

    solution=Solution()
    print(solution.isSymmetric(root))




