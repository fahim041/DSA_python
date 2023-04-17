package linkedlist;

public class LinkedList {
    class Node{
        int val;
        Node next;

        Node(int val){
            this.val = val;
            next = null;
        }
    }

    Node head;

    public void insertFirst(int val){
        Node newNode = new Node(val);
        if(head == null) {
            head = newNode;
        }else {
            newNode.next = head;
            head = newNode;
        }
    }

    public void insertLast(int val){
        Node newNode = new Node(val);
        if(head == null){
            head = newNode;
            return;
        }

        Node tmp = head;
        while(tmp.next != null){
            tmp = tmp.next;
        }

        tmp.next = newNode;
    }

    public boolean deleteLast(){
        if(count() < 1 ){
            return false;
        } else{
            Node tmp = head;
            while(tmp.next.next != null){
                tmp = tmp.next;
            }
            tmp.next = null;
            return true;
        }
    }

    public boolean deleteNode(int index){
        if(count() <= 0){
            return false;
        }

        Node tmp = head;
        int n = 0;
        while(n < index - 1){
            tmp = tmp.next;
            n++;
        }
        Node deletedNode = tmp.next;
        tmp.next = tmp.next.next;
        deletedNode.next = null;

        return true;
    }

    public void sort(){
        if(head == null){
            return;
        }

        Node current = head;
        Node next = null;

        while(current != null){
            next = current.next;

            while(next != null){
                if(current.val > next.val){
                    int tmp = current.val;
                    current.val = next.val;
                    next.val = tmp;
                }
                next = next.next;
            }
            current = current.next;
        }
    }

    public int count(){
        int n = 0;
        if(head == null){
            return 0;
        } else{
            Node tmp = head;
            while(tmp != null){
                n++;
                tmp = tmp.next;
            }

            return n;
        }
    }

    public void print(){
        Node tmp = head;
        while(tmp != null){
            System.out.print(tmp.val+ "->");
            tmp = tmp.next;
        }
    }
}
