package queue;

import java.util.ArrayList;
import java.util.Arrays;

public class PriorityQueue {
    private int[] items = new int[5];
    private int count;

    public void enqueue(int item){
        if(count == items.length)
            throw new IllegalStateException();

        int i;
        for(i = count -1; i >= 0; i--){
            if(items[i] > item)
                items[i+1] = items[i];
            else
                break;
        }

        System.out.println("count "+count);
        System.out.println("i " + i);

        items[i+1] = item;
        count++;
    }

    public int dequeue(){
        if(count == 0)
            throw new IllegalStateException();
        return items[--count];
    }

    public boolean isEmpty(){
        return count == 0;
    }

    @Override
    public String toString() {
        return Arrays.toString(items);
    }
}
