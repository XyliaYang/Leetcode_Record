# @Time : 2020/2/23 17:03
# @Author : Xylia_Yang
# @Description :合并两个排序的链表

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        merge_node=None
        if l1.val<=l2.val:
            merge_node=l1
            merge_node.next=self.mergeTwoLists(l1.next,l2)
        else:
            merge_node=l2
            merge_node.next=self.mergeTwoLists(l1,l2.next)

        return  merge_node


