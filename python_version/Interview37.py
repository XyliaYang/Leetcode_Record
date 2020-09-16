# @Time : 2020/3/3 16:10
# @Author : Xylia_Yang
# @Description :

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return  '$'

        return  str(root.val)+','+self.serialize(root.left)+','+self.serialize(root.right)



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes =iter(data.split(','))
        return self.deserialize_tree(nodes)

    def deserialize_tree(self,nodes):

        item=next(nodes)

        if item=='$':
            return
        root=TreeNode(item)
        root.left=self.deserialize_tree(nodes)
        root.right=self.deserialize_tree(nodes)

        return root



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
if __name__=='__main__':
    head=TreeNode(1)
    head.left=TreeNode(2)
    head.right=TreeNode(3)
    head.left.left=TreeNode(4)
    head.right.left=TreeNode(5)
    head.right.right=TreeNode(6)

    codec=Codec()
    str=codec.serialize(head)
    print(str)
    new_head=codec.deserialize(str)
    print('h')

