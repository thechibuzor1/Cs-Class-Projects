import java.util.Scanner;

public class Binary_converter {

    static String tobinary(int num) {
        String binary = "";
        while (num > 0) {
            binary = (num % 2) + binary;
            num /= 2;
        }
        return binary;
    }

    public static void main(String[] args) {
        Scanner xt = new Scanner(System.in);
        System.out.println("BINARY CONVERTER");
        Object res;
        do {
            System.out.println("ENTER THE DECIMAL INTERGER: ");
            int n = xt.nextInt();
            System.out.println(n + " IN BINARY IS " + tobinary(n));

            System.out.println("CONTINUE? (YES/NO)");
            res = xt.next();
        } while (res.equals("yes"));

    }
}