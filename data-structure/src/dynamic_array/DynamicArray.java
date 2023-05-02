package dynamic_array;

public class DynamicArray {
    private int[] items;
    private int count;
    public DynamicArray(int length){
        items = new int[length];
    }

    public void insert(int value){
        if(items.length == count){
            int[] newArray = new int[count * 2];

            for(int i = 0; i < count; i++)
                newArray[i] = items[i];

            items = newArray;
        }
        items[count++] = value;
    }

    public void removeAt(int index){
        if(index < 0 || index >= count)
            throw new IllegalArgumentException("index out of bound");
        for (int i = index; i < count; i++)
            items[i] = items[i+1];
        count--;
    }

    public int indexOf(int item){
        for(int i = 0; i < items.length; i++){
            if(items[i] == item)
                return i;
        }
        return -1;
    }

    public void print(){
        for (int i = 0; i < count; i++){
            System.out.println(items[i]);
        }
    }
}