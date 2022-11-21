import java.lang.Math;

public class Circle extends Shape {
    double pi = Math.PI;

    Circle(int x) {
        this.width = x;
    }

    public void area() {
        double res = pi * width * width;
        System.out.println("THE AREA IS: " + res);
    }
}
