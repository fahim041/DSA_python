import dynamic_array.DynamicArray;
import queue.Queue;

public class Main {
    public static void main(String[] args) {
        var array = new DynamicArray(2);
        array.insert(4);
        array.insert(5);
        array.insert(6);
        array.insert(7);
        array.insert(8);
        System.out.println(array.indexOf(70));
    }
}