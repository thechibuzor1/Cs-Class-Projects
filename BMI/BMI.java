package BMI;

import java.util.Scanner;

public class BMI {
    protected String name;
    private int weight;
    private double height;

    // constructor
    BMI(String name) {
        this.name = name;
    }

    // name setter
    public void setName(String n) {
        this.name = n;
    }

    // name getter
    public String getName() {
        return name;
    }

    // weight setter
    public void setWeight(int w) {
        this.weight = w;
    }

    // weight getter
    public int getWeight() {
        return weight;
    }

    // height setter
    public void setHeight(Double h) {
        this.height = h;
    }

    // height getter
    public double getHeight() {
        return height;
    }

    public static double get_results(int a, double b) {
        b = b * b;
        double result = a / b;
        return result;
    }

    public static void main(String[] args) {
        Scanner xt = new Scanner(System.in);
        System.out.println("BMI CHECKER");
        System.out.println("ENTER YOUR DETAILS: ");
        System.out.println("YOUR NAME: ");
        String name1 = xt.nextLine();
        BMI p = new BMI(name1);
        System.out.println("YOUR HEIGHT(IN METRES): ");
        double height1 = xt.nextDouble();
        p.setHeight(height1);
        System.out.println("YOUR WEIGHT(IN KILOS): ");
        int weight1 = xt.nextInt();
        p.setWeight(weight1);

        System.out.println(name1 + " YOUR BMI IS: ");
        System.out.println(get_results(weight1, height1));
    }

}
