public class CircularQueue {
    //    Add = Enque
//    Remove = Deque
//    Peek = Front

    //    Implementing CircularArray
    static class Queue{
        static int arr[];
        static int size;
        static int rear = -1;
        static int front = -1;


        Queue(int n){
            arr = new int[n];
            this.size = n;
        }
        public static boolean isEmpty(){
            return rear == -1 && front == -1 ;
        }

        public static boolean isFull(){
            return (rear+1)%size ==front;
        }

        //         Enque
        public static void add(int data){
            if (isFull()){
                System.out.println("Queue is full");
                return;
            }

            if (front == -1){
                front =0;
            }
            rear=(rear+1)%size;
            arr[rear]=data;
        }
        //    dequeue
        public static int remove(){
            if (isEmpty()){
                System.out.println("Queue is empty");
                return -1;
            }
            int result = arr[front];
           if(rear == front){
               rear = front = -1;
           }else{
               front = (front+1) % size;
           }

            return result;
        }

        //    peek
        public static int peek(){
            if (isEmpty()){
                System.out.println("Queue is empty");
                return -1;
            }
            return arr[front];
        }
    }

    public static void main(String[] args) {
        Queue q = new Queue(5);
        q.add(10);
        q.add(5);
        q.add(3);
        q.add(2);
        System.out.println(q.peek());
    }
}
