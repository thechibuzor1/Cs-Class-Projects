class something {
    public static double sum(double a, double b) {
        return a + b;
    }

    // overloading
    public static int sum(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        double a = 2.7;
        double b = 5.8;
        int c = 5;
        int g = 7;
        System.out.println(sum(g, b));
        System.out.println(sum(a, g));

    }
}

// overriding
class soemthingNew extends something {
    public static double sum(double a, double b) {
        return 2 * b;
    }

    public static void main(String[] args) {
        double a = 2.7;
        double b = 5.8;
        int c = 5;
        int g = 7;
        System.out.println(sum(g, b));

    }
}