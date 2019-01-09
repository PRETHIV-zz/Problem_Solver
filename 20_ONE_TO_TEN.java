/* package whatever; // don't place package name! */
 
import java.util.*;
import java.lang.*;
import java.io.*;
 
/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
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
