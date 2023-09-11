import org.w3c.dom.ls.LSOutput;

import java.util.Scanner;

public class RecPattern {
    static void solid_rect(int r, int c){
        for (int i=0;i<r;i++){
            for (int j=0;j<c;j++){
                System.out.print("*");
            }
            System.out.println();
        }

    }

    public static void main(String[] args) {
        System.out.println("Please Enter Number of Rows : ");
        Scanner scanner = new Scanner(System.in);
        int r = scanner.nextInt();
        System.out.println("Please Enter Number of Columns : ");
        int c = scanner.nextInt();
        solid_rect(r,c);
    }

}
