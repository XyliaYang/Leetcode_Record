# @Time : 2020/3/13 8:54
# @Author : Xylia_Yang
# @Description :

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return

        a_count=0
        b_count=0
        p_a=headA
        p_b=headB

        while p_a:
            a_count+=1
            p_a=p_a.next

        while p_b:
            b_count+=1
            p_b=p_b.next

        p_a=headA
        p_b=headB
        if a_count>b_count:
            sub=a_count-b_count
            while sub:
                p_a=p_a.next
                sub-=1
        else:
            sub=b_count-a_count
            while sub:
                p_b=p_b.next
                sub-=1

        while p_a!=p_b:
            p_a=p_a.next
            p_b=p_b.next

        return  p_a


