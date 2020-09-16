import javax.sound.midi.Soundbank;
import java.awt.*;

class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}


public class Interview35 {
    public Node copyRandomList(Node head) {
        if(head==null)
            return null;

        Node p=head;
        while (p!=null){
            Node new_node=new Node(p.val);
            new_node.next=p.next;
            p.next=new_node;
            p=p.next.next;
        }

        p=head;
        while (p!=null &&p.next !=null){
            if(p.random !=null){
                p.next.random=p.random.next;
            }
            p=p.next.next;
        }

        p=head;
        Node new_node=p.next;
        while (p!=null && p.next!=null){
            Node temp=p.next;
            p.next=p.next.next;
            if(p.next!=null){
                temp.next=p.next.next;
            }
            p=p.next;
        }
        return new_node;
    }

    public  static void main(String[] args) {
        Node head=new Node(7);
        head.next=new Node(13);
        head.next.next=new Node(11);
        head.next.next.next=new Node(10);
        head.next.next.next.next=new Node(1);

        head.next.random=head;
        head.next.next.random=head.next.next.next.next;
        head.next.next.next.random=head.next.next;
        head.next.next.next.next.random=head;

        Interview35 interview35=new Interview35();
        Node new_head=interview35.copyRandomList(head);
        System.out.println(new_head);
    }
}
