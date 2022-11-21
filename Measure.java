import java.util.Scanner;
class Measure{
    static int min(int a, int b){
        if  (a < b){
            return a; //defining a method that takes two int argumnets and returns the smaller int value 
        }else{
            return b;
        }
    }

    static int max(int a, int b){
        if (a > b){
            return a; // defining a second method  that also takes two arguments and returns the larger int value
        }else{
            return b;
        }
    }

    public static void main(String[] args){
        Scanner xt = new Scanner(System.in);
        while (1 > 0){
            System.out.println("What mathematical operation do you want to calculate");
            System.out.println("min - minimum \nmax - maximum");
            String user_input = xt.nextLine();
            if (user_input== "min"){
                System.out.println("Enter the numbers; ");
                int x = xt.nextInt();
                int y = xt.nextInt();
                System.out.println("The smaller number is: "+ min(x,y));
                continue;

            }
            else if (user_input.equals("max")){
                System.out.println("Enter the numbers; ");
                int x = xt.nextInt();
                int y = xt.nextInt();
                System.out.println("The larger number is: "+ max(x,y));
                continue;

            }else{
                System.out.println("Invalid input");
            }
        }
    }
}