
class Link{
private int size;
Link(){
    this.size = 0;
}
    Node head ;

    class Node{

        int data;
        Node next;

        Node(int data){
            this.data = data;
            this.next = null;
            size++;         }
    }
    public void addNode(int data){
        Node newNode = new Node(data);
        if (head == null){
            head = newNode;
            return;
        }
        newNode.next = head;
        head = newNode;

    }

    public void addlast(int data){
        Node newNode = new Node(data);
        if (head == null){
            head = newNode;
            return;
        }
        Node currNode = head;
        while (currNode.next != null){
             currNode = currNode.next;

        }
        currNode.next = newNode;
    }


    public void deleteFirst(){
        if (head == null){
            System.out.println("the list is empty");
            return;
        }
        size--;
        head = head.next;
    }

    public void deleteLast(){
        if (head == null){
            System.out.println("the list is empty");
            return;
        }
        size--;
        if (head.next == null){
            head = null;
            return;
        }

        Node secondLast = head;
        Node last = head.next;
        while (last.next != null){
            last = last.next;
            secondLast = secondLast.next;
        }
        secondLast.next = null;
    }
    public void printList(){
        if (head == null){
            System.out.println("The list is empty");
            return;
        }
        Node currenNode = head;
        while(currenNode != null){
            System.out.print(currenNode.data + "--->");


            currenNode = currenNode.next;

        }
        System.out.print("Null");
    }

public int linkedListseze (){
        return size;
}
    public static void main(String[] args) {
        Link list = new Link();

        list.addNode(2);

        list.addNode(1);
        list.addNode(0);
        list.addlast(3);


        list.printList();
        System.out.println();
        System.out.println(list.linkedListseze());

    }
}






