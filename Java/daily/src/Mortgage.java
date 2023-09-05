import java.sql.SQLOutput;
import java.text.NumberFormat;
import java.util.Scanner;

public class Mortgage {
    public static void main(String[] args){
        final byte MONTHS_IN_YEAR = 12;
        final byte PERCENT = 100;
        Scanner scanner = new Scanner(System.in);

        System.out.print("Principle : ");
        int principle = scanner.nextInt();

        System.out.print("annual interest rate : ");
        float annualInterest = scanner.nextFloat();
        float monthlyInterest = annualInterest / PERCENT / MONTHS_IN_YEAR;

        System.out.print("Period (Years) : ");
        byte years = scanner.nextByte();
        int numberOfPayments = years * MONTHS_IN_YEAR;

        double mortgage = principle * (monthlyInterest*Math.pow(1+monthlyInterest,numberOfPayments))
                /(Math.pow(1+monthlyInterest,numberOfPayments)-1);

        String mortgageFromated = NumberFormat.getCurrencyInstance().format(mortgage);
        System.out.println("Mortgae " + mortgageFromated);

    }
}
