public class QueueWithLinkedList {

    //    Add = Enque
//    Remove = Deque
//    Peek = Front

    //    Implementing Queue with linkedlist

    static class Node{
        int data;
        Node next;

        Node(int data){
            this.data = data;
            next = null;
        }
    }
    static class Queue{
        static Node head = null;
        static Node tail = null;

        public static boolean isEmpty(){
            return head == null && tail == null;
        }

        //         Enque
        public static void add(int data){
            Node newNode = new Node(data);
            if (tail==null){
                tail = head = null;
                return;
            }
            tail.next = newNode;
            tail = newNode;

        }
        //    dequeue
        public static int remove(){
            if (isEmpty()){
                System.out.println("Queue is empty");
                return -1;
            }

            int front = head.data;
            if (head==tail){
                tail = null;
            }
            head = head.next;
            return front;

        }

        //    peek
        public static int peek(){
            if (isEmpty()){
                System.out.println("Queue is empty");
                return -1;
            }
            return head.data;
        }
    }

    public static void main(String[] args) {
        QueueBasic.Queue q = new QueueBasic.Queue(5);
        q.add(10);
        q.add(5);
        q.add(3);
        q.add(2);
        System.out.println(q.peek());
    }
}
