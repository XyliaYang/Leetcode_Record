# @Time : 2020/2/23 16:09
# @Author : Xylia_Yang
# @Description :反转链表

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre_node=None
        cur_node=head
        pHead=None

        while cur_node:
            next_node=cur_node.next
            if not next_node: #若到了尾节点
                pHead=cur_node

            cur_node.next=pre_node
            pre_node=cur_node
            cur_node=next_node

        return pHead




