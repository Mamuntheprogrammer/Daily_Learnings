public class Day1 {

//    how javacode execute

// Java Compilation process :  source code --> Java compiler (Janvac) in JDK --> Bytecode
// Java execution process   : Bytecode --> (JVM from java JRE) --> native code (Machine code / binary code )





    public static void main(String[] args) {

        System.out.println(args);

    }

//    public : public is a access modifier keyword that specifies the visibility of the method. here public means that
//    the main can be accessed from outside of the class so Jre can access the class .

//    static : This static keyword indicates that the main method belong to the class itself, rather than to an instance of the class
//    for static use can call the method by the class name , u do not need to create instance to run the method.

//    void : This is the return type of main method,that means the main method does not return any values

//    main: This is the name of the method. In Java, the main method is the entry point of a Java program.
//    When you run a Java program, the Java Virtual Machine (JVM) looks for this method and starts executing the code inside it.

//    (String[] args): This is the method's parameter list. In this case, the main method takes a single parameter,
//    which is an array of strings named args. This parameter allows you to pass command-line arguments to your Java program when you run it.
//    args is an array of strings that can hold command-line arguments provided by the user.



}



