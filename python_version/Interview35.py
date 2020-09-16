# @Time : 2020/3/3 9:04
# @Author : Xylia_Yang
# @Description : 复杂链表的复制


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return

        p=head
        while p:
            new_node=Node(p.val,p.next,None)
            p.next=new_node
            p=p.next

        p=head
        while p.next:
            p.next.random=p.random.next
            p=p.next

            if p.next:
                p=p.next

        p=head
        new_head=p.next
        while p.next:
            temp=p.next
            p.next=p.next.next
            if p.next:
                temp.next=p.next.next
            p=p.next

        return new_head

