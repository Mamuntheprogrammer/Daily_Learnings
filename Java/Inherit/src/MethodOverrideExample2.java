class Shape {
    void draw() {
        System.out.println("Drawing a shape.");
    }
}

class Circle extends Shape {
    @Override
    void draw() {
        System.out.println("Drawing a circle.");
    }
}

public class MethodOverrideExample2 {
    public static void main(String[] args) {
        Shape shape = new Circle(); // Polymorphism
        shape.draw(); // Calls the overridden method in Circle
    }
}

//This line of code will call the draw method of the Circle class
//because shape is currently pointing to a Circle object,
//even though its reference type is Shape.

