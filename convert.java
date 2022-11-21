import java.util.Scanner;

class Convert {
    public static double getFahrenheit(double celsius) {
        double fahrenheit;
        fahrenheit = celsius * 9;
        fahrenheit = fahrenheit / 5;
        fahrenheit = fahrenheit + 32;

        return fahrenheit;
    }

    public static double getCelsius(double fahrenheit) {
        double celsius;
        celsius = fahrenheit - 32;
        celsius = celsius * 5;
        celsius = celsius / 9;

        return celsius;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int resCon;
        do {
            System.out.println("Enter the operation to perform: (1)C->F (2)F->C");
            int res = input.nextInt();
            if (res == 1) {
                System.out.println("Enter your value in Celsius: ");
                Double res1 = input.nextDouble();
                try {
                    System.out.println(res1 + "C is: " + getFahrenheit(res1) + "F");
                } catch (Exception e) {
                    System.out.println("Something went wrong.");
                }

            } else if (res == 2) {
                System.out.println("Enter your value in Fahrenheit: ");

                try {
                    Double res2 = input.nextDouble();
                    System.out.println(res2 + "F is: " + getCelsius(res2) + "C");
                } catch (Exception e) {
                    System.out.println("Something went wrong.");
                }

            } else {
                System.out.println("Error");
            }

            System.out.println("Run a new operation? (1)Yes (2) quit");
            resCon = input.nextInt();
        } while (resCon == 1);
    }

}