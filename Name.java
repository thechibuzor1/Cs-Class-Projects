import java.util.Scanner;
public class Name {
    static void Say_hey(String x){
        System.out.println("Hey "+ x);
    }
    public static void main(String[] args){
Scanner xt = new Scanner(System.in);
System.out.println("Whats your name? ");
String name = xt.nextLine();

for(int i=0; i<3; i++){
Say_hey(name);
}
}
}