import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner scan=new Scanner(System.in);
		String s1,s2="",s3="";
		s1=scan.nextLine();
		int f=0;
		String s[]=s1.split(" ",2);
		s2=s[0];
		s3=s[1];
		if(s2.compareTo(s3)==0){
			System.out.print(s3);
		}
		else if(s2.compareTo(s3)>0){
			System.out.print(s2);
		}
		else if(s3.compareTo(s2)>0){
			System.out.print(s3);
		}
	}
}
