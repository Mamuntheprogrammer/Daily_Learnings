
public class LinkedList1 {
    private Node head; // Reference to the head of the linked list

    // Constructor to initialize an empty linked list
    public LinkedList1() {
        head = null;
    }

    // Node class to represent individual nodes in the linked list
    private class Node {
        int data; // Data stored in the node
        Node next; // Reference to the next node

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    // Method to add a new node to the beginning of the linked list
    public void addToFront(int data) {
        Node newNode = new Node(data); // Create a new node with the given data
        newNode.next = head; // Set the next of the new node to the current head
        head = newNode; // Update the head to be the new node
    }

    // Method to print the elements of the linked list
    public void display() {
        Node current = head; // Start from the head of the list
        while (current != null) {
            System.out.print(current.data + " "); // Print the data in the current node
            current = current.next; // Move to the next node
        }
        System.out.println(); // Print a newline to separate from other output
    }

    public static void main(String[] args) {
        LinkedList1 list = new LinkedList1(); // Create a new linked list

        list.addToFront(3); // Add elements to the front of the list
        list.addToFront(2);
        list.addToFront(1);

        list.display(); // Print the elements of the list (1 2 3)
    }
}
