# @Time : 2020/2/19 19:39
# @Author : Xylia_Yang
# @Description : 链表中倒数第k个节点

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

# 将链表写成类是方便增删
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

    def showList(self):
        cur=self.head
        while cur is not None:
            print(cur.data,end=' ')
            cur=cur.next
        print()

def  find_Kth_tail(pHead,k):
    if pHead is None or  k<=0:
        return
    gap=0

    pre=pHead
    cur=pHead
    while gap<k-1:
        if pre.next is None:
            return
        pre=pre.next
        gap+=1

    while pre.next is not None:
        pre=pre.next
        cur=cur.next
    return cur.data


if __name__=='__main__':

    link_list=Linked_list()
    for i in  range(8):
        link_list.add(i)
    link_list.showList()

    print(find_Kth_tail(link_list.head,0))































