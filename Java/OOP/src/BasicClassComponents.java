public class BasicClassComponents {

//    Instance variable / Instance fields
    private String name;
    private int age;


//    constructor

    public BasicClassComponents(String n, int a){
        name = n;
        age = a;
    }

//    Mutator or setMethod or method

    public void setName(String name){
        this.name = name;
    }

//    Accessor method
    public String getName(){
        return this.name +" " +this.age;
    }
}
