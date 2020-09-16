# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 9:28
# @Author  : Xylia_Yang
# @Description ：


# 面试6题：
# 题目：从尾到头打印链表
# 输入一个链表，从尾到头打印链表每个节点的值。

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class  Linked_list:
    def __init__(self):
        self.head=None

    def add(self,data):
        """
        从表头插入新结点
        :param data:
        :return:
        """
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode

    def remove(self,data):
        """
        删除链表中第一个值等于data的节点
        :param data:
        :return:
        """
        pre=None
        p=self.head

        while p is not None:
            if p.data==data:
                break
            pre=p
            p=p.next

        if pre is None: # 要删除的是头结点
            self.head=self.head.next
        else:
            pre.next=p.next

## 思路一：遍历链表之后将所有元素入栈，再从栈顶输出元素
def PrintListReversingly(pHead):
    NodeStack=[]

    pNode=pHead
    while pNode !=None:
        NodeStack.append(pNode)
        pNode=pNode.next

    while len(NodeStack)>0:
        node=NodeStack.pop()
        print(node.data)

## 思路二：递归，递归本质就是栈
def PrintListRecursively(pHead):
    pNode=pHead

    if pNode is not  None:
        if pHead.next is not  None:
            PrintListRecursively(pHead.next)
        print(pNode.data)



if __name__=='__main__':

    linkList=Linked_list()
    for i in range(5):
        linkList.add(i)

    PrintListReversingly(linkList.head)
    PrintListRecursively(linkList.head)










