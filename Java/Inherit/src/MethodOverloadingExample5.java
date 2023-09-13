class Calculator {
    int add(int a, int b) {
        return a + b;
    }

    double add(double a, double b) {
        return a + b;
    }

    String add(String a, String b) {
        return a + b;
    }
}

public class MethodOverloadingExample5 {
    public static void main(String[] args) {
        Calculator calculator = new Calculator();

        int result1 = calculator.add(5, 7);
        System.out.println("Sum (int): " + result1);

        double result2 = calculator.add(3.5, 2.5);
        System.out.println("Sum (double): " + result2);

        String result3 = calculator.add("Hello, ", "World!");
        System.out.println("Concatenation: " + result3);
    }
}
