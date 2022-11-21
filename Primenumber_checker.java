import java.util.Scanner;
public class Primenumber_checker {

    //checker method
    static void checker(int num){
        if(num <= 1){
            System.out.println("NOT A PRIME NUMBER!");
        }else{
            //iterating through range 2 - num
            for(int i =2; i < num; i++){
                if(num % i == 0){
                    System.out.println("NOT A PRIME NUMBER!");
                    break;
                }else{
                    System.out.println("PRIME NUMBER");
                    break;
                }
            }
        }
    }
    public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    System.out.println("PRIME NUMBER CHECKER");
    System.out.println("Enter the number: ");
    int num = input.nextInt();

    checker(num); 
    
    //the while loop
    System.out.println("Do you want to continue operations on this? yes/no");
    String res = input.next();
    if(res.equals("yes")){
        while(res.equals("yes")){
        System.out.println("Enter the number: ");
        int n = input.nextInt();
        checker(n);

        //ending the loop
        System.out.println("Continue or end?");
        String res1 = input.next();
        if(res1.equals("end")){
            break;
        }else if(res1.equals("continue")){
            continue;
        }else{ 
            System.out.println("ERROR!");
        }

        }
    }else if(res.equals("no")){
        System.exit(0);
    }
    }
}
