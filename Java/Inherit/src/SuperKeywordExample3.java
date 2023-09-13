class Parent {
    String name = "Parent";

    void display() {
        System.out.println("Name: " + name);
    }
}

class Child extends Parent {
    String name = "Child";

    @Override
    void display() {
        super.display(); // Calls the display method of the Parent class
        System.out.println("Name: " + name);
    }
}

public class SuperKeywordExample3 {
    public static void main(String[] args) {
        Child child = new Child();
        child.display();
    }
}
