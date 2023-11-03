import java.util.Scanner;

public class GrayCode {

    public static String convert(String str) {
        String text = str;
        char MSB = text.charAt(0);
        String Gray = "";
        for (int i = 0; i < text.length() - 1; i++) {
            String grayUnit;
            if (text.charAt(i) == text.charAt(i + 1)) {
                grayUnit = "0";
            } else {
                grayUnit = "1";
            }
            Gray = Gray + grayUnit;

        }
        return (MSB + Gray);
    }

    static String tobinary(int num, int numberOfBits) {
        String binary = "";
        while (num > 0) {
            binary = (num % 2) + binary;
            num /= 2;
        }
        if (binary.length() < numberOfBits) {
            int remainingBits = numberOfBits - binary.length();
            String zeroes = "0".repeat(remainingBits);
            binary = zeroes + binary;
        }
        return binary;
    }

    public static void main(String[] args) {
        Scanner xt = new Scanner(System.in);
        System.out.println("n-bit Gray code table generator");
        Object res;
        do {
            System.out.println("ENTER THE NUMBER OF BITS: ");
            int numberOfBits = xt.nextInt();
            int lastElement = (int) (Math.pow(2, numberOfBits)) - 1;

            System.out.printf("%-10s %-10s %-10s%n", "Decimal", "Binary", "Gray code");
            for (int i = 0; i <= lastElement; i++) {
                System.out.printf("%-10s %-10s %-10s%n", i, tobinary(i, numberOfBits),
                        convert(tobinary(i, numberOfBits)));
            }
            System.out.println("CONTINUE? (YES/NO)");

            res = xt.next();
        } while (res.equals("yes"));

    }
}
