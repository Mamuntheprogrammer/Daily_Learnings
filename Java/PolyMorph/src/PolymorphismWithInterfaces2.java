interface Shape {
    double area();
}

class Circle implements Shape {
    double radius;

    Circle(double radius) {
        this.radius = radius;
    }

    @Override
    public double area() {
        return Math.PI * radius * radius;
    }
}

class Rectangle implements Shape {
    double width, height;

    Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    @Override
    public double area() {
        return width * height;
    }
}

public class PolymorphismWithInterfaces2{
    public static void main(String[] args) {
        Shape shape1 = new Circle(5.0);
        Shape shape2 = new Rectangle(4.0, 3.0);

        System.out.println("Area of Circle: " + shape1.area());       // Outputs: Area of Circle: 78.53981633974483
        System.out.println("Area of Rectangle: " + shape2.area());    // Outputs: Area of Rectangle: 12.0
    }
}


//    Polymorphism with Interfaces:
//    Java allows polymorphism through interfaces.
//    Multiple classes can implement the same interface,
//    and objects of these classes can be treated as instances of the interface.