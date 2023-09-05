import java.util.Scanner;

public class FizBuzz {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int userInput = scanner.nextInt();

        if (userInput%5==0 && userInput%3==0){
            System.out.println("FizzBuzz");
        } else if (userInput%5==0) {
            System.out.println("Fizz");

        } else if (userInput%3==0) {
            System.out.println("Buzz");
        }
        else {
            System.out.println(userInput);
        }


    }
}
