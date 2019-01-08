import java.io.*;
public class Stack{
    private int top=-1;
    private int a[]=new int[10];
    public void push(int d){
        if(top<9){
            a[++top]=d;
            
        }
        else{
            System.out.println("Stack is Full");
            
        }
        
    }
    public int pop(){
        if(top>-1){
            return a[top--];
        }
        else{
            System.out.print("Stack is empty");
            return -1;
            
        }
        
    }
    

public static void main(String args[] ) throws Exception {
        /*
         * Read input from stdin and provide input before running

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        int N = Integer.parseInt(line);
        for (int i = 0; i < N; i++) {
            System.out.println("hello world");
        }
        */
        Stack s=new Stack();
        for(int i=0;i<15;i++){
            s.push(i);
        }
        for(int i=0;i<15;i++){
            System.out.println(s.pop());
        }
    }
}
