# @Time : 2020/7/30 21:30
# @Author : Xylia_Yang
# @Description :
"""
1.树中序遍历的递归：
栈S
p=根节点root

while(p || S):
  while(p):
    p入栈
    p=p.left
  node=S出栈
  访问node
  p=node.right
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root) :
        if not root:
            return []

        inorder=[]
        travelStack=[]

        p=root
        while(p or travelStack):
            while(p):
                travelStack.append(p)
                p=p.left

            tmpNode=travelStack.pop()
            inorder.append(tmpNode.val)
            p=tmpNode.right

        return inorder


if __name__=='__main__':
    solution=Solution()
    root=TreeNode(1)
    root.right=TreeNode(2)
    root.right.left=TreeNode(3)

    print(solution.inorderTraversal(root))



