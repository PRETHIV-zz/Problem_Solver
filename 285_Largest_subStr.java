/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		String s,ans="",t1="";
		Scanner ss=new Scanner(System.in);
		s=ss.next();
		t1=s;
		for(int i=0;i<s.length();i++){
			String temp="";
			for(int j=i+1;j<s.length();j++){
				temp=temp+s.charAt(j);
			}
			if(temp.compareTo(t1)>0){
				ans=temp;
				t1=ans;
				break;
			}
		}
		System.out.println(ans);
	}
}
