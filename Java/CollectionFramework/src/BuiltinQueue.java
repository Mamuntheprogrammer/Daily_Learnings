import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.Queue;

public class BuiltinQueue {

// we can use linkedlist and arraydeque both for implementing Queue 

    public static void main(String[] args) {
//        Queue<Integer> q = new LinkedList<>();
        Queue<Integer> q = new ArrayDeque<>();
        q.add(10);
        q.add(5);
        q.add(3);
        q.add(2);
        System.out.println(q.peek());
    }
}
