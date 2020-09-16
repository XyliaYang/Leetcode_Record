
public class L2 {
    public static void main(String[] args) {
        ListNode l1=new ListNode(5);
        ListNode l2=new ListNode(5);

        Solution solution=new Solution();
        ListNode res=solution.addTwoNumbers(l1, l2);
        while(res!=null){
            System.out.println(res.val);
            res=res.next;
        }
    }

}


class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}


class Solution{
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode pre=new ListNode(0);
        ListNode cur=pre;
        int carryNum=0;
        int sum=0;
        // int num=0;

        while(l1!=null || l2!=null || carryNum!=0){
            sum=(l1==null?0:l1.val)+(l2==null?0:l2.val)+carryNum;
            cur.next=new ListNode(sum%10);
            carryNum=sum/10;

            if(l1!=null){
                l1=l1.next;
            }
            if(l2!=null){
                l2=l2.next;
            }

            cur=cur.next;
        }

        return pre.next;
    }
}
