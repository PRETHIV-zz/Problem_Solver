//I am prethiv
#include<stdio.h>
#include<string.h>
int main()
{
char s1[10000],s2[10000],temp;


int n,len;
scanf("%s%d",s1,&n);
strcpy(s2,s1);
int i;
len=strlen(s1);
for(i=0;s1[i]!='\0';i++){
    s1[(i+n)%len]=s2[i];
}
printf("%s",s1);
return 0;
}
