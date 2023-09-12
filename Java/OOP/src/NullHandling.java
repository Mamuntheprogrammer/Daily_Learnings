import java.util.Objects;

public class NullHandling {

private String nam;
    public NullHandling(String name){

//        name = Objects.requireNonNull(name,"The name cannot be null");
//        System.out.println(name);

//        or

        Objects.requireNonNull(nam,"not supported");
        nam = name;
        System.out.println(nam);

    }




    public static void main(String[] args) {
        String str = null;
//        System.out.println(str.length());

//        how to handle this null pointer exception


//        There are two solutions. The “permissive” approach is to turn a null argument
//        into an appropriate non-null value:

//        if (n == null) name = "unknown"; else name = n;


        if (str == null) str = "unknow";else str = "working";

        System.out.println(str);

//        As of Java 9, the Objects class has a convenience method for this purpose:
//
//          public Employee(String n, double s, int year, int month, int day)
//        {
//            name = Objects.requireNonNullElse(n, "unknown"); }

        NullHandling obj = new NullHandling(null);


    }
}
