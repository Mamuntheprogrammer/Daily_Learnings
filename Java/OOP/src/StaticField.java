public class StaticField {

//    the static field belongs to the class but not any individual object
    public static String name;

//    The id field is belong to the every instance which created from class StaticField

    private int id;


    public static String getName(){
        return "name";
    }


    public static void main(String[] args) {
        System.out.println(getName());
    }
}


