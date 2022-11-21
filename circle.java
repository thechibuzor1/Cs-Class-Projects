class Circle {
    private double radius;

    /* constructor set initial values on object creation. */
    Super Circle(double r) {
        this.radius = r;
    }

    /* getter: used to ..get variables that are private in a class */
    public double getRadius() {
        return this.radius;
    }

    /* setter: used to set values for private variables */
    public void setRadius(double radius) {
        this.radius = radius;
    }

    /*
     * method overloading: creating methods with the same name in the same class but
     * have different functionalities or number of arguments or different number of
     * arguments or data structure
     */
    public static int getPow(int x, int n) {
        /*
         * here getPow is type int, returns an integer, and has 2 arguments of type int
         */
        int start = x;

        while (n > 1) {
            x = x * start;
            n = n - 1;
        }
        return x;
    }

    public static double getPow(double x, int n) {
        /*
         * here getPow is type double, returns a double, and has 2 arguments of type
         * double
         */
        double start = x;

        while (n > 1) {
            x = x * start;
            n = n - 1;
        }
        return x;
    }

    public double getArea() {
        /*
         * the arguments passsed to getPow determines which version is used. here radius
         * is a double
         */
        return getPow(this.radius, 2) * 3.142;

    }

    public static void main(String[] args) {
        Circle one = new Circle(5.0); /* creating a circle object named "one" with radius 5 */
        one.setRadius(7.0); /* setting the radius as 7 */
        System.out.println("Radius: " + one.getRadius());
        System.out.println("Area: " + one.getArea());
        System.out.println("5 raised to the power of 2 is: " + getPow(5, 2));
        System.out.println("9.7 raised to the power of 0 is: " + getPow(9.7, 0));
    }
}

class SmallerCircle extends Circle {
    /* overridding: when a subclass is created from a class */
    public static double getPow(double x, int n) {
        /*
         * here getPow is type double, returns a double, and has 2 arguments of type
         * double
         */

        return x + 50;
    }

    public static void main(String[] args) {

        System.out.println(getPow(6.0, 2));
    }
}