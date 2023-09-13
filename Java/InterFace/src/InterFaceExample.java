interface Drawable {
    void draw();
}
class Circle implements Drawable {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    public void draw() {
        System.out.println("Drawing a circle with radius " + radius);
    }
}


interface Playable {
    void play();
}

class Piano implements Drawable, Playable {
    @Override
    public void draw() {

    }

    @Override
    public void play() {

    }
    // Implement methods for both Drawable and Playable
    // ...
}



public class InterFaceExample {


}
