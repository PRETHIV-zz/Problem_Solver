/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	public static String sortpret(String s){
		char c[]=s.toCharArray();
		Arrays.sort(c);
		String st=new String(c);
		return st;
	}
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner ss=new Scanner(System.in);
		int n;
		n=ss.nextInt();
		String s[]=new String[n];
		String s1[]=new String[n];
		int c=0;
		for(int i=0;i<n;i++){
			s[i]=ss.next();
			s1[i]=sortpret(s[i]);
		}
		for(int i=0;i<n;i++){
			
			if(s1[0].equals(s1[i])){
				c++;
			}
		}
		System.out.println(c);
	}
}
