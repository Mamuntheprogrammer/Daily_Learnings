
abstract class Shape {
    abstract double area();
    abstract double perimeter();
}

class Circle extends Shape {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    @Override
    double area() {
        return Math.PI * radius * radius;
    }

    @Override
    double perimeter() {
        return 2 * Math.PI * radius;
    }
}




interface Animal {
    void eat();
    void makeSound();
}

class Dog implements Animal {
    @Override
    public void eat() {
        System.out.println("Dog is eating.");
    }

    @Override
    public void makeSound() {
        System.out.println("Woof! Woof!");
    }
}

class Cat implements Animal {
    @Override
    public void eat() {
        System.out.println("Cat is eating.");
    }

    @Override
    public void makeSound() {
        System.out.println("Meow!");
    }
}



public class AbstractionExample1 {
    public static void main(String[] args) {
        Shape shape = new Circle(5.0);
        System.out.println("Circle Area: " + shape.area());
        System.out.println("Circle Perimeter: " + shape.perimeter());

        Animal dog = new Dog();
        dog.eat();
        dog.makeSound();

        Animal cat = new Cat();
        cat.eat();
        cat.makeSound();
    }
}
