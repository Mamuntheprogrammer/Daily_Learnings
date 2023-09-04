import java.util.Scanner;

public class Day2 {
    public static void main(String[] args){
//        Constant uses final keyword , use upper letter
        final float PI = 3.14F;

//        Order of operation () * / + -
//        Casting : byte > short > int > long > float > double
//        Implicit casting
        int x = 10;
        double y = x + 1.2;
//        Explicit casting
        int w = (int) y + 2;

//        Integer.parseInt();
//        Float.parseFloat();
//        Double.parseDouble();


//        Math class
        int a = Math.round(1.1F);

//        Math.floor();
//        Math.ceil();
//        Math.random();
//        Math.max();
//        Math.min();

        int result = (int) (Math.random()*100);
        System.out.println(result);


//        user input
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter your name : ");
        String name = scanner.nextLine().trim();
        System.out.println("My name is "+ name);

    }
}
