#include<stdio.h>
#include<string.h>
int main(){
char s[10000],*s1=malloc(10000);
scanf("%s",s);
int i;
s1=strrev(s);
printf("%s",s1);
return 0;
}
