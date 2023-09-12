
import java.time.LocalDate;

class Emp{
    private String name;
    private double salary;
    private LocalDate hireDay;

//    Constructor
    public Emp(String n,double s, int year, int month, int day){
        name = n;
        salary = s;
        hireDay = LocalDate.of(year,month,day);

    }

    public String getName(){
        return this.name;
    }

}





public class Employee {
    public static void main(String[] args) {
// making an array of objects
        Emp staff[] = new Emp[3];

        staff[0] = new Emp("farhan",1200,2023,05,25);
        staff[1] = new Emp("farhan1",1200,2023,05,25);
        staff[2] = new Emp("farhan2",1200,2023,05,25);


        for (Emp e : staff){
            System.out.println(e.getName());
        }
    }
}


