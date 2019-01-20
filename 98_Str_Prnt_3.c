//string prnt 3rdchar
#include<stdio.h>
int main(){
char s[1000];
int i;
scanf("%s",s);
for(i=0;s[i]!='\0';i++){
    if(i==0||(i%3)==0){
    printf("%c",s[i]);
    }
}
return 0;
}
