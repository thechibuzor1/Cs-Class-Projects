import java.util.Scanner;

public class Blop {

   public static void main(String[] args) {
       try(Scanner x = new Scanner(System.in)){   
       System.out.println("enter the number abeg...");
       int n = x.nextInt();
       //your code goes here
       while(n >= 0 ){
           if(n == 0){
               System.out.println(n);
           }
           if(n % 3 ==  0){
               n -= 1;
               continue;             
           }
           System.out.println(n);
           n -= 1;
       }
    
       }
    }}
