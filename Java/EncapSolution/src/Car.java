
//It refers to the bundling of data (attributes) and methods (functions)
// that operate on that data into a single unit called a class.


// https://www.youtube.com/shorts/MVnK1iYv0LE


public class Car {
    // Attributes (fields)
    private String make;
    private String model;
    private int year;

    // Constructor
    public Car(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }

    // Getter methods
    public String getMake() {
        return make;
    }

    public String getModel() {
        return model;
    }

    public int getYear() {
        return year;
    }

    // Setter methods
    public void setMake(String make) {
        this.make = make;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public void setYear(int year) {
        this.year = year;
    }



    public static void main(String[] args) {
        Car myCar = new Car("Toyota", "Camry", 2022);

        // Accessing attributes via getter methods
        System.out.println("Make: " + myCar.getMake());
        System.out.println("Model: " + myCar.getModel());
        System.out.println("Year: " + myCar.getYear());

        // Modifying attributes via setter methods
        myCar.setMake("Honda");
        myCar.setModel("Accord");
        myCar.setYear(2023);

        // Displaying updated information
        System.out.println("Make: " + myCar.getMake());
        System.out.println("Model: " + myCar.getModel());
        System.out.println("Year: " + myCar.getYear());
    }


}


//
//2. Access Modifiers:
//
//        Access modifiers control the visibility of class members.
//        private restricts access to the member only within the class.


//        3. Getter and Setter Methods:
//
//        Getter methods provide read access to private attributes.
//        Setter methods provide write access to private attributes.