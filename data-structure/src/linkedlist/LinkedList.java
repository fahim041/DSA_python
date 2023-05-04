package linkedlist;

import java.util.NoSuchElementException;

public class LinkedList {
    class Node{
        private int value;
        private Node next;

        public Node(int value){
            this.value = value;
        }
    }

    private Node first;
    private Node last;

    public void addLast(int item){
        var node = new Node(item);
        if(isEmpty()){
            first = last = node;
        } else {
            last.next = node;
            last = node;
        }
    }

    public void addFirst(int item){
        var node = new Node(item);
        if(isEmpty()){
            first = last = node;
        } else {
            node.next = first;
            first = node;
        }
    }

    public void removeFirst(){
        if(isEmpty()) throw new NoSuchElementException();

        if(first == last){
            first = last = null;
            return;
        }

        var head = first;
        first = head.next;
        head.next = null;
    }

    public void removeLast(){
        if(isEmpty()) throw new NoSuchElementException();

        if(first == last){
            first = last = null;
            return;
        }

        var current = first;
        while(current.next.next != null){
            current = current.next;
        }

        current.next = null;
        last = current;
    }

    public int indexOf(int item){
        int index = 0;
        var current = first;

        while(current != null){
            if(current.value == item){
                return index;
            }
            current = current.next;
            index++;
        }
        return -1;
    }

    public boolean contains(int item){
        return indexOf(item) != -1;
    }

    public int size(){
        if(isEmpty()) return 0;
        var current = first;
        int count = 0;
        while(current != null){
            count++;
            current = current.next;
        }

        return count;
    }

    public void print(){
        if(first == null)
            System.out.println("list is empty");
        var current = first;
        while(current != null){
            System.out.print(current.value+ "-> ");
            current = current.next;
        }
    }

    public int[] toArray(){
        if(isEmpty()) return new int[0];
        int[] arr = new int[size()];
        int index = 0;
        var current = first;
        while(current != null){
            arr[index] = current.value;
            current = current.next;
            index++;
        }

        return arr;
    }

    public void reverse(){
        Node prev = null;
        var current = first;
        first = last;
        last = first;

        while(current != null){
            var next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
    }

    private boolean isEmpty(){
        return first == null;
    }

}
