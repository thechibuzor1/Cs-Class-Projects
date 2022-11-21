import java.util.Scanner;

public class Mainclass {
    public static void main(String[] args) {
        Scanner xt = new Scanner(System.in);
        System.out.println("What is your avatar's name? ");
        String A_name = xt.nextLine();
        Person one;
        one = new Person(A_name);
        System.out.println("How old are they? ");
        int A_age = xt.nextInt();
        one.setAge(A_age);
        System.out.println(one.getName() + " is " + one.getAge() + " years old");

        birthday(one);
        System.out.println(one.getName() + " is " + one.getAge() + " years old");

    }

    static void birthday(Person j) {
        j.setAge(j.getAge() + 1);
    }
}
