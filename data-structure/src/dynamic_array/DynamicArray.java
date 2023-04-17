package dynamic_array;

public class DynamicArray {
    private int arr[];
    private int capacity;
    private int current;

    public DynamicArray(){
        arr = new int[1];
        capacity = 1;
        current = 0;
    }

    public void push(int data){
        if(current == capacity){
            int[] temp = new int[2 * capacity];
            for(int i = 0; i < capacity; i++){
                temp[i] = arr[i];
            }
            capacity *= 2;
            arr = temp;
        }
        arr[current] = data;
        current++;
    }

    public void push(int data, int index){
        if(index == capacity){
            push(data);
        } else {
            arr[index] = data;
        }
    }

    public void pop(){
        current--;
    }

    public int get(int index){
        if(index < current){
            return arr[index];
        }
        return -1;
    }

    public void print(){
        for(int i = 0; i < current; i++){
            System.out.println(arr[i]);
        }
    }

    public int size(){
        return this.current;
    }

    public int getCapacity(){
        return this.capacity;
    }
}
