class Vehicle {
    String type;

    Vehicle(String type) {
        this.type = type;
    }
}

class Car extends Vehicle {
    String model;

    Car(String type, String model) {
        super(type); // Call the constructor of the superclass
        this.model = model;
    }
}

public class ConstructorInheritanceExample4 {
    public static void main(String[] args) {
        Car car = new Car("Sedan", "Toyota");
        System.out.println("Type: " + car.type);
        System.out.println("Model: " + car.model);
    }
}
