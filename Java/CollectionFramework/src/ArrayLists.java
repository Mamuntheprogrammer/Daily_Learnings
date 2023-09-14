import java.util.*;

public class ArrayLists {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
//        Add Elements
        list.add(1);
        list.add(2);
        list.add(3);
        System.out.println(list);


//        Get elements
        System.out.println(list.get(1));

//        Add element in between

        list.add(2,51);
        System.out.println(list);


//        update or modify the element

        list.set(0,100);
        System.out.println(list);

//        delete or remove the list
        list.remove(2);
        System.out.println(list);

//        find the size of the array
        System.out.println(list.size());

//        loops
        for (int i=0 ; i<list.size();i++){
            System.out.println(list.get(i));
        }

//        sorting array
        Collections.sort(list);
        System.out.println(list);
    }
}
