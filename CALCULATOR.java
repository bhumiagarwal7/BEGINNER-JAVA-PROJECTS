import java.util.*;
class Main{
    public static void main(String[] args){
        Scanner sc= new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int n = sc.nextInt();
        switch(n)
        {
            case 1: int sum = a+b;
            System.out.println("Sum="+sum);
            break;
            case 2: int diff = a-b;
            System.out.println("Difference="+diff);
            break;
            case 3: int prod = a*b;
            System.out.println("Product="+prod);
            break;
            case 4: int rem = a%b;
            System.out.println("Remainder="+rem);
            break;
            default: System.out.println("Invalid input"); 
        }
    }
}