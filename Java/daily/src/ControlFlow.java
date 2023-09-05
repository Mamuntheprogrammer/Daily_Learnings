import org.w3c.dom.ls.LSOutput;

public class ControlFlow {
    public static void main(String[] args){
        int salary = 100_000;
        boolean ishighIncome = false;
        if (salary>10){
            ishighIncome = true;
        } else{
            ishighIncome = false;
        }

//         it can be simplyfy like this
        boolean islowIncome = (salary < 10000);

//        using ternary operator
        String className = (salary > 10000) ? "High":"low";
        System.out.println(className);

//        simple switch case
        String role = "Admin";
        switch (role){
            case "dmin":
                System.out.println("ok");
                break;
            default:
                System.out.println("Not found the role");


        }


    }
}
