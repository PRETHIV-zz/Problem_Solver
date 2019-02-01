//finally the rock is comeback
#include<stdio.h>
#include<string.h>
int main()
{
int n;
int c=0;
char p[100];
scanf("%d",&n);
char s[n][1000];
int i;
for(i=0;i<n;i++){
    scanf("%s",s[i]);
}
scanf("%s",p);
char *l;
for(i=0;i<n;i++){
   l=strstr(s[i],p);
   int pos=l-s[i];
   if(pos==0){
    c+=1;
   }
}
printf("%d",c);
return 0;
}
