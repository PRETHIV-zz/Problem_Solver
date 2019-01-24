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
		int n,ans=1;
		Scanner ss=new Scanner(System.in);
		n=ss.nextInt();
		if(n==0){
			System.out.println(ans);
		}
		else{
			while(n>=1){
				ans*=n;
				n--;
			}
			System.out.println(ans);
		}
	}
}
