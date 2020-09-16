
from functools import cmp_to_key

class solution45:
    def printMinNum(self,nums):
        nums.sort(key=cmp_to_key(self.compareFun))

        res=""
        for num in nums:
            res+=str(num)
        return res


    def compareFun(self,num1,num2):
        str1=str(num1)+str(num2)
        str2=str(num2)+str(num1)

        if str1>str2:
            return 1
        elif str1<str2:
            return -1
        else:
            return 0    

        




class solution54:
    def findKth(self,root,k):
        self.count=0
        self.node=None

        self.doFind(root,k)

        return self.node

    def doFind(self,root,k):
        if not root:
            return 
        
        if root.left:
            self.doFind(root.left,k)
        
        self.count+=1
        if self.count==k:
            self.node=root
        
        if root.right:
            self.doFind(root.right,k)


class solution36:
    def convert(self,root):
        if not root:
            return None
        
        self.lastNode=None

        self.convertCore(root)
        pNode=self.lastNode

        while pNode.left:
            pNode=pNode.left
        
        return pNode
    

    def convertCore(self,root):
        if not root:
            return
        
        if root.left:
            self.convertCore(root.left)
        
        root.left=self.lastNode
        if not self.lastNode:
            self.lastNode.right=root
        
        if root.right:
            self.convertCore(root.right)

        
        


class TreeNode:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None


class solution37:
    def serialize(self,root):
        res=[]
        self.doSerialize(root,res)

        return res
    
    def doSerialize(self,root,res):
        if not root:
            res.append('$')
            return
        
        res.append(root.val)
        self.doSerialize(root.left,res)
        self.doSerialize(root.right,res)

    def deSerialize(self,res_ls):
        nodes=iter(res_ls)

        return self.doDeserialize(nodes)
    
    def doDeserialize(self,nodes):
        item=next(nodes)

        if item=='$':
            return
        root=TreeNode(item)

        root.left=TreeNode(nodes)
        root.right=TreeNode(nodes)

        return root
        


if __name__ =='__main__':
    solution_37=solution37()
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.left.left=TreeNode(4)
    root.left.right=TreeNode(5)
    root.left.right.left=TreeNode(6)
    root.right.right=TreeNode(7)

    print(solution_37.serialize(root))




class Solution:
    def isSymmetric(self,root):
        return self.sysmentric(root,root)

    def sysmentric(self,root1,root2):
        if not root1 and not root2:
            return True
        if (not root1 and root2) or (root1 and not root2):
            return False
        if root1.val !=root2.val:
            return True
        
        return self.sysmentric(root1.left,root2.right) and   self.sysmentric(root1.right,root2.right)

        


class solution:
    def dfs(self,root):
        if not root:
            return 0
        
        left=self.dfs(root.left)
        right=self.dfs(root.right)

        if abs(left-right)>1:
            self.isbalanced=False
        
        return 1+max(left+right)


    def isBalanced(self,root):
        self.isbalanced=True
        self.dfs(root)

        return self.isbalanced



class  solution:
    def isAvgTree(self,root):
        if not root:
            return False
        
        is_avg,_=self.isAvgandHeight(root)
        
        return is_avg
    
    def isAvgandHeight(self,root):
        if not root:
            return True,0
        
        left,left_height=self.isAvgandHeight(root.left)
        right,right_height=self.isAvgandHeight(root.right)

        if left and right and abs(left_height-right_height)<=1:
            return True,1+max(left_height,right_height)
        
        return False,1+max(left_height,right_height)
        



def treeHeight(root):
    if not root:
        return 0
    
    return 1+max(treeHeight(root.left),treeHeight(root.right))


class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def pathSum(self,root,sum):
        if not root:
            return []
        
        res=[]
        stack=[]
        cur_sum=0

        self.getSumPath(root,stack,cur_sum,sum,res)
        return res
    
    def getSumPath(self,root,stack,cur_sum,sum,res):

        cur_sum+=root.val
        if self.isLeaf(root) and cur_sum==sum:
            stack.append(root.val)

            path=[]
            for i in stack:
                path.append(i)
            
            res.append(path)
            
        
        if not root.left:
            self.getSumPath(root.left,stack,cur_sum,sum,res)
        
        if not root.right:
            self.getSumPath(root.right,stack,cur_sum,sum,res)
        
        stack.pop()
        cur_sum-=root.val

        return 

    def isLead(self,root):
        if root.left or root.right:
            return False
        else:
            return True

            
        



def  printBinaryTree(root):
    if not root:
        return
    tmp=[]

    tmp.append(root)

    while len(tmp)>0:
        node=tmp.pop(0)
        print(node.data)
        
        if root.left:
            tmp.append(root.left)
        if root.right:
            tmp.append(root.right)
    

def commonNode(l1,l2):
    if not l1 or not l2:
        return
    
    len_l1=0
    p1=l1
    while p1:
        len_l1+=1
        p1=p1.next
    
    len_l2=0
    p2=l2
    while p2:
        len_l2+=1
        p2=p2.next

    common_node=None
    if l1>l2:
        d=l1-l2
        while d>0:
            l1=l1.next
            d-=1
    else:
        d=l2-l1
        while d>0:
            l2=l2.next
            d-=1
    
    while l1 and l2:
        if l1==l2:
            common_node=l1
            break
        l1=l1.next
        l2=l2.next
        
    return common_node


class Node:
    def __init__(self,data,next,random):
        self.data=data
        self.next=next
        self.random=random
        

def copyComplex(head):
    if not head:
        return 
    
    p_cur=head
    while p_cur:
        p_next=p_cur.next
        p_cur.next=Node(p_cur.data,p_cur.next,None)
        p_cur=p_next
    
    p_cur=head
    while p_cur:
        p_cur.next.random=p_cur.random.p_next
        p_cur=p_cur.next.p_next
    
    new_head=head.next
    p_cur=head
    new_cur=new_head
    while p_cur:
        if new_cur.next:
            p_cur.next=new_cur.next
            new_cur.next=new_cur.next.next
            p_cur=p_cur.next
            new_cur=new_cur.next
    
    return new_head


        


def mergeLinkedList(p1,p2):
    if not p1:
        return p2
    if not p2:
        return p1

    cur_node=None
    if p1.data<p2.data:
        cur_node=p1
        cur_node.next=mergeLinkedList(p1.next,p2)
    else:
        cur_node=p2
        cur_node.next=mergeLinkedList(p1,p2.next)
    
    return cur_node





