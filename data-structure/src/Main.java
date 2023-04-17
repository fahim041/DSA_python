import dynamic_array.DynamicArray;
import queue.Queue;

public class Main {
    public static void main(String[] args) {
        Queue queue = new Queue();
        queue.push(4);
        queue.push(10);
        queue.push(6);

        queue.pop();

        queue.print();
    }
}