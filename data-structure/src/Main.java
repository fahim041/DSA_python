import linkedlist.LinkedList;

public class Main {
    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        list.insertFirst(2);
        list.insertFirst(10);
        list.insertFirst(7);
        list.insertLast(21);
        list.insertFirst(4);

        list.sort();

        list.print();
    }
}