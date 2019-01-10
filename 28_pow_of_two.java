/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;
import java.lang.Math.*;
/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner scan=new Scanner(System.in);
		int n,on;
		n=scan.nextInt();
		on=n;
		int c=-1;
		while(n>0){
			c++;
			n=n/2;
		}
		if(Math.pow(2,c)==on){
			System.out.println("yes");
		}
		else{
			System.out.println("no");
		}
	}
}
