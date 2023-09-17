import java.util.*;
public class BultinLinkList {

    public static void main(String[] args) {

    LinkedList<String> list = new LinkedList<String>();
    list.addFirst("a");
    list.addFirst("b");
    list.addLast("hi");
    list.removeFirst();
    list.removeLast();
    System.out.println(list);
    System.out.println(list.size());

    for(int i = 0; i<list.size();i++){
        System.out.println(list.get(i));
    }




    }
}
