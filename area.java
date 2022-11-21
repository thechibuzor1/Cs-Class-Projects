import java.lang.Math;
import java.util.Scanner;

public class area {
    /*
     * sqrt(s(s-a)(s-b)(s-c))
     * s = 1/2(a+b+c)
     */

    static void cal(int a, int b, int c) {
        Double s;
        s = 0.5 * (a + b + c);
        Double t1 = s - a;
        Double t2 = s - b;
        Double t3 = s - c;

        Double t4 = t1 * t2 * t3;
        Double t5 = s * t4;

        Double tri_area = Math.sqrt(t5);
        System.out.println("THE AREA IS:  " + tri_area);
    }

    public static void main(String[] args) {
        System.out.println("AREA OF A TRIANGLE");
        Scanner xt = new Scanner(System.in);
        System.out.println("ENTER THE LENGTH OF THE SIDES: ");
        System.out.println("a: ");
        int a = xt.nextInt();
        System.out.println("b: ");
        int b = xt.nextInt();
        System.out.println("c: ");
        int c = xt.nextInt();
        cal(a, b, c);

    }

}
