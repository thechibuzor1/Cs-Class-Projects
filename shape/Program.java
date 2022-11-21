import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        Scanner xt = new Scanner(System.in);
        int res;
        do {

            System.out.println("CHOOSE AN OPERATION: ");
            System.out.println("AREA OF A SQUARE(ENTER 1):\nAREA OF A CIRCLE(ENTER 2):\nQUIT(ENTER 3):");
            res = xt.nextInt();

            if (res == 1) {
                System.out.println("ENTER THE WIDTH OF THE SQUARE: ");
                int W = xt.nextInt();
                Square s;
                s = new Square(W);
                s.area();
                continue;
            }
            if (res == 2) {
                System.out.println("ENTER THE RADIUS OF THE CIRCLE: ");
                int r = xt.nextInt();
                Circle c;
                c = new Circle(r);
                c.area();
                continue;
            }
            if (res == 3) {
                System.out.println("GOODBYE");
                System.exit(0);
            } else {
                System.out.println("INVALID INPUT!");
            }

        } while (res != 3);
    }
}