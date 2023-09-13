class Calculator {
    int add(int a, int b) {
        return a + b;
    }

    double add(double a, double b) {
        return a + b;
    }
}

public class MethodOverloadingPolymorphism3 {
    public static void main(String[] args) {
        Calculator calc = new Calculator();

        System.out.println("Sum of ints: " + calc.add(5, 3));         // Outputs: Sum of ints: 8
        System.out.println("Sum of doubles: " + calc.add(2.5, 3.7)); // Outputs: Sum of doubles: 6.2
    }
}

//    Polymorphism can also occur with method overloading when multiple methods with the same name but different parameters exist in a class.
//    The appropriate method is called based on the arguments provided.
// note : all the same method must present in one class
// this is compile time polymorphism
