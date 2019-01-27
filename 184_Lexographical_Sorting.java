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
		int n=ss.nextInt();
		String s[]=new String[n];
		for(int i=0;i<n;i++){
			s[i]=ss.next();
		}
		for(int i=0;i<n;i++){
			for(int j=i+1;j<n;j++){
				if(s[i].compareTo(s[j])>0){
					String t;
					t=s[i];
					s[i]=s[j];
					s[j]=t;
				}
			}
		}
		
			System.out.print(s[0]);
		
	}
}
