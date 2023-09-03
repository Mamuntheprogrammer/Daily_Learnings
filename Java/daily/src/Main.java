import java.util.Date;

public class Main {
    public static void main(String[] args) {

//        Primitive data types
        int viewCount = 123_123_123; // in every three digit we can use _ for clear visibility
        long viewCount2 = 3_123_123_123L;
        float price = 10.30F;
        char letter ='A';

        boolean isEligible = true;

//        Reference Data types
        Date now = new Date();
        System.out.println(now);

        Point point1 = new Point(2,3);
        Point point2 = point1;
        point2.x = 10;
        System.out.println(point1);

//         String in Java ( String are reference type in java
//        String is immutable in Java

        String name = new String("Mamun");
//        or
        String name2 = "Mamun2";
        System.out.println(name + " " +name2);

//        Escape Sequences
        System.out.println("Hello \"Mamun\" ");

//        Arrays

        int[] numbers = new int[5];
        int[] numbers2 = {1,2,3};
        System.out.println(Arrays.toString(numbers));
        System.out.println(Arrays.toString(numbers2));

//        this is for test purpose 





    }
}