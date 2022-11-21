import java.util.Scanner;

class Permutaionycombination {
    public static int factorial(int n) {
        if (n < 1) {
            return 1;
        } else {
            return n * factorial(n - 1);
        }
    }

    public static int permutation(int n, int r) {

        if (r > n) {
            throw new IllegalArgumentException("INVALID FORMAT!");
        }

        return factorial(n) / factorial(n - r);
    }

    public static int combination(int n, int r) {
        if (r > n) {
            throw new IllegalArgumentException("INVALID FORMAT!");
        }
        return factorial(n) / (factorial(n - r) * factorial(r));
    }

    public static void main(String[] args) {
        Scanner xt = new Scanner(System.in);
        String re;

        do {
            try {
                System.out.println("What operation do you wan to perform: ");
                System.out.println("(P)permutaion\n(C)combination\n(F)factorial: ");
                char res = xt.next().charAt(0);
                if (res == 'p') {
                    System.out.println("n: ");
                    int n = xt.nextInt();
                    System.out.println("r: ");
                    int r = xt.nextInt();
                    System.out.println("The permuation is: " + permutation(n, r));

                } else if (res == 'c') {
                    System.out.println("n: ");
                    int n = xt.nextInt();
                    System.out.println("r: ");
                    int r = xt.nextInt();
                    System.out.println("The combination is: " + combination(n, r));
                } else if (res == 'f') {
                    System.out.println("n: ");
                    int n = xt.nextInt();
                    System.out.println(n + "factorial is: " + factorial(n));
                } else {
                    System.out.println("INALID INPUT!");
                }

            } catch (IllegalArgumentException ex) {
                System.out.println(ex.getMessage());
            }

            System.out.println("(Yes)continue?\n(No)no ");
            re = xt.next();
        } while (re.equals("yes"));

    }
}