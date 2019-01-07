import java.io.*;
import java.util.*;
public class Chkvowel{

public static void main(String ag[]){
  Scanner s=new Scanner(System.in);
  char c;
  int k=0;
  c=s.next().charAt(0);
  char cmp[]="bcdfghjklmnpqrstvwxyz".toCharArray();
  if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u'||c=='A'||c=='E'||c=='I'||c=='O'||c=='U'){
    System.out.println("Vowel");
    k=1;
  }
  else{
    for(int i=0;i<cmp.length;i++){
    if(c==cmp[i]){
      System.out.println("Consonant");
      k=1;
      break;
    }
    }
  }
  if(k!=1){
  System.out.println("invalid");
  }
}

}
