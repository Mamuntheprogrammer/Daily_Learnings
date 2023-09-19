import java.lang.reflect.Array;

public class StackBasic {
//    Operation
//    Pop
//    push
//    peek

//    There are three ways of implement the stack
//    Array
//    ArrayList
//    Linkedlist

    static class Node{
        int data;
        Node next;
        public Node(int data){
            this.data = data;
            next = null;
        }
    }

    static class Stack{
        public static Node head;
        public static boolean isEmpty(){
            return head==null;
        }
        public static void push(int data){
            Node newNode = new Node(data);
            if(isEmpty()){
                head = newNode;
                return;
            }
            head.next = newNode;
            head = newNode;
        }

        public static int pop(){
            if(isEmpty()){
                return -1;
            }
            int top = head.data;
            head = head.next;
            return top;
        }

        public static int peek(){
            if(isEmpty()){
                return -1;
            }
            return head.data;
        }
    }

    public static void main(String[] args) {
 Stack s = new Stack();
 s.push(25);
 s.push(23);
 s.push(12);
        System.out.println(s.peek());
    }
}
