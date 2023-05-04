import queue.PriorityQueue;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        PriorityQueue queue = new PriorityQueue();
        queue.enqueue(5);
        queue.enqueue(3);
        queue.enqueue(6);
        queue.enqueue(1);
        queue.dequeue();
    }
}