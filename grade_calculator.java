import java.util.Scanner;

class Grade {
    /*
     * 70 - above -A
     * 60 - 69 - B
     * 50 - 59 - C
     * 45 - 49 - D
     * 40 - 44 - E
     * 0 - 39 - F
     */

    static void check(int num) {
        if (num >= 70) {
            System.out.println("THE STUDENT'S GRADE IS: A");
        } else if (num >= 60 && num <= 69) {
            System.out.println("THE STUDENT'S GRADE IS: B");
        } else if (num >= 50 && num <= 59) {
            System.out.println("THE STUDENT'S GRADE IS: C");
        } else if (num >= 45 && num <= 49) {
            System.out.println("THE STUDENT'S GRADE IS: D");
        } else if (num >= 40 && num <= 44) {
            System.out.println("THE STUDENT'S GRADE IS: E");
        } else if (num >= 0 && num <= 39) {
            System.out.println("THE STUDENT'S GRADE IS: F");
        }
    }

    public static void main(String[] args) {
        Scanner xt = new Scanner(System.in);
        System.out.println("ENTER THE STUDENT'S GRADE: ");
        int num = xt.nextInt();
        check(num);
        System.out.println("CONTINUE? (YES/NO)");
        String res = xt.next();
        if (res.equals("yes")) {
            while (res.equals("yes")) {
                System.out.println("ENTER THE STUDENT'S GRADE: ");
                int n = xt.nextInt();
                System.out.println("");
                check(n);
                System.out.println("Continue or end?");
                String res1 = xt.next();
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