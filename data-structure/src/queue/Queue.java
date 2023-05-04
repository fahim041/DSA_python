package queue;

import java.util.Arrays;

public class Queue {
    private int[] items;
    private int rear;
    private int count;
    private int front;

    public Queue(int capacity){
        items = new int[capacity];
    }

    public void enqueue(int item){
        if(count == items.length)
            throw new IllegalArgumentException();
        items[rear++] = item;
        count++;
    }

    public int dequeue(){
        var item = items[front];
        items[front++] = 0;
        count--;
        return item;
    }

    @Override
    public String toString() {
        return Arrays.toString(items);
    }
}
