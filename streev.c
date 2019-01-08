#include<stdio.h>
int main(){
char s[10000],s1[10000];
scanf("%s",s);
int i;
for(i=strlen(s);i>=0;i--){
    s1[strlen(s)-i]=s[i-1];
}
printf("%s",s1);
return 0;
}

