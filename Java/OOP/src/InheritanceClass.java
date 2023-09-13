public class InheritanceClass {
    public String name = "";
    public int age = 0;

    public InheritanceClass(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getInfo() {
        return this.name + " " + this.age;
    }

    public static void main(String[] args) {
        Manager obj = new Manager("John", 30,"cumilla");
        System.out.println(obj.getInfo());


    }
}

class Manager extends InheritanceClass {


    private String area;

    public Manager(String name, int age, String division) {
        super(name, age);
        String area = division;
    }
public String getDivision(){
        return this.area;
}

}
