package queue;

public class Queue {
    class Node{
        int val;
        Node next;

        public Node(int val){
            this.val = val;
            next = null;
        }
    }

    Node head;

    public void push(int data){
        Node newNode = new Node(data);
        if(head == null){
            head = newNode;
            return;
        }

        Node temp = head;
        while(temp.next != null){
            temp = temp.next;
        }
        temp.next = newNode;
    }

    public void pop(){
        if(head == null){
            return;
        }
        Node temp = head;
        head = temp.next;
        temp.next = null;
    }

    public void print(){
        Node temp = head;
        while(temp != null){
            System.out.println(temp.val);
            temp = temp.next;
        }
    }
}
