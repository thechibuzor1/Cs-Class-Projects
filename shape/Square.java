public class Square extends Shape {
    Square(int x) {
        this.width = x;
    }

    public void area() {
        int res = width * width;
        System.out.println("THE AREA IS: " + res);
    }
}
