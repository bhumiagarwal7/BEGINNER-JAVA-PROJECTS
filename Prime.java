import java.util.*;
public class Prime {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int c=0;
        if(n==1)
           System.out.println(n+" is neither a prime nor a composite number");
        else
        {
           for(int i=1;i<=n;i++)
           {
            int rem = n%i;
            if(rem==0)
               c++;
           }
        if(c==2)
            System.out.println(n+" is a prime number");
        else
            System.out.println(n+" is not a prime number");
        }
    }
}
