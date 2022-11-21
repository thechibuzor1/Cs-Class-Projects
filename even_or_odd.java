import java.util.Scanner;

public class even_or_odd {
    static String check(int num) {

        if (num % 2 == 0) {
            return num + " is an even number";
        } else {
            return num + " is an odd number";
        }
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number: ");
        int num = input.nextInt();
        System.out.println(check(num));

        // the while loop
        System.out.println("Do you want to continue operations on this? yes/no");
        String res = input.next();
        if (res.equals("yes")) {
            while (res.equals("yes")) {
                System.out.println("Enter the number: ");
                int n = input.nextInt();
                System.out.println(check(n));

                // ending the loop
                System.out.println("Continue or end?");
                String res1 = input.next();
                if (res1.equals("end")) {
                    break;
                } else if (res1.equals("continue")) {
                    continue;
                } else {
                    System.out.println("ERROR!");
                }

            }
        } else if (res.equals("no")) {
            System.exit(0);
        }
    }

}
