import java.io.*;
import java.util.*;
public class HelloWorld{

     public static void main(String []args){
        Scanner ss=new Scanner(System.in);
        int i;
        i=ss.nextInt();
        if(i>=1&&i<=10){
            System.out.println("yes");
        }
        else{
            System.out.println("no");
        }
     }
}
