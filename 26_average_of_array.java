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
		int n;
		Scanner scan=new Scanner(System.in);
		n=scan.nextInt();
		int a[]=new int[n];
		int sum=0;
		for(int i=0;i<n;i++){
			a[i]=scan.nextInt();
			sum+=a[i];
		}
		System.out.print(sum/n);
	}
}
