//prethiv
import java.io.*;
import java.util.*;
public class Alphano{

public static void main(String args[]){
  char cmp[]="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".toCharArray();
  Scanner s=new Scanner(System.in);
  char c;
  c=s.next().charAt(0);
  int k=0;
  for(int i=0;i<cmp.length;i++){
      if(c==cmp[i]){
        k=1;
        System.out.println("Alphabet");
        break;
      }
  }
  if(k=0){
    System.out.println("No");
  }
}
}
