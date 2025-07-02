import java.util.*;
public class Marks {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = 1;
        do{
            
            System.out.println("Enter marks");
            int m = sc.nextInt();
            if(m>=90){
                System.out.println("This is good");
            }else if(m<90&&m>=60){
                System.out.println("This is also good");
            }else {
                System.out.println("This is good as well");
            }
            System.out.println("Enter 1 to display remarks and 0 to stop");
            n = sc.nextInt();
        }
        while(n==1);
    }

}
