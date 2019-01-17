//Encode string
#include<stdio.h>
int main(){
char *s=malloc(10000);
scanf("%s",s);
int i;
for(i=0;s[i]!='\0';i++){
    if(s[i]>=65&&s[i]<=90){
        int n=s[i];
        n=(n+3)%91;
        if(n>64){
            s[i]=n;
        }
        else{
            n=n+65;
            s[i]=n;
        }
        }
    if(s[i]>=97&&s[i]<=122){
        int n=s[i];
        n=(n+3)%123;
        if(n>96){
            s[i]=n;
        }
        else{
            n=n+97;
            s[i]=n;
                    }
    }
}
printf("%s",s);
return 0;
}
