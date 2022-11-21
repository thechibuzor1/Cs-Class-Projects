import java.util.Scanner;

public class Reverse {
    public static void main(String[] args){
    Scanner xt = new Scanner(System.in);
    System.out.println("Enter the sentence to reverse: ");
    String words = xt.nextLine();
    char[] arr = words.toCharArray();
    String xc = "";
    for (char i : arr){
        xc = i + xc;
    }
    System.out.println(xc);
    }
}
