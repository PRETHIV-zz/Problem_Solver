#include<stdio.h>
#include<string.h>
int main(){
char *s=malloc(10000);
scanf("%s",s);
int i;
s=strrev(s);
printf("%s",s);
return 0;
}
